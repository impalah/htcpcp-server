# ####################################################################
# # Application configuration
# ####################################################################


# # Recover secret and format
# # Recuperar el secreto de AWS Secrets Manager
# data "aws_secretsmanager_secret_version" "db_read_credentials" {
#   secret_id = var.read_database_secret_id
# }

# # Parsear el JSON del secreto a un mapa
# locals {
#   db_read_credentials = jsondecode(data.aws_secretsmanager_secret_version.db_read_credentials.secret_string)
# }

# # Formatear la cadena de conexión
# locals {
#   db_read_connection_string = format(
#     "Host=%s:%s;Database=%s;Username=%s;Password=%s",
#     local.db_read_credentials["host"],
#     local.db_read_credentials["port"],
#     local.db_read_credentials["dbname"],
#     local.db_read_credentials["username"],
#     local.db_read_credentials["password"]
#   )
# }

# # Uso de la cadena de conexión
# output "db_read_connection_string" {
#   value     = local.db_read_connection_string
#   sensitive = true
# }


# # Environment variables

# locals {
#   api_service_environment_values = [
#     { ConnectionStrings__DatabaseRead = local.db_read_connection_string },
#     { ConnectionStrings__DatabaseApplication = local.db_read_connection_string },
#     { AWS__logGroup = module.services_logs_group.logs_group_name },
#     { AWS__Cognito__UserPoolId = module.cognito.aws_cognito_user_pool-userpool_id },
#     { AWS__Cognito__ClientId = module.cognito.aws_cognito_user_pool-user_client_id },
#     { Jwt__Authority = format("https://%s", module.cognito.url_base) },
#     { Jwt__MetadataAddress = format("https://%s/.well-known/openid-configuration", module.cognito.url_base) },
#     { Jwt__TokenValidationParameters__ValidIssuer = format("https://%s", module.cognito.url_base) },
#     { Jwt__TokenValidationParameters__ValidateIssuer = false },
#     { Jwt__TokenValidationParameters__ValidateAudience = false },
#     { Jwt__TokenValidationParameters__ValidateLifetime = false },
#     { Jwt__TokenValidationParameters__ValidateIssuerSigningKey = false },
#     { SESSettings__Host = var.ses_email_host },
#     { SESSettings__Port = var.ses_email_port },
#     { SESSettings__DisplayName = var.ses_email_display_name },
#     { SESSettings__SenderEmail = var.ses_email_sender_email },
#     { SESSettings__IdentityARN = var.ses_email_identity_arn },
#     { SESSettings__ConfirmationBaseUrl = var.ses_email_confirmation_base_url },
#     { SESSettings__emailRoberlo = var.ses_email_roberlo },
#     { SESSettings__Username = var.ses_email_username },
#     { SESSettings__Password = var.ses_email_password },
#     { LOCATION = "/" },
#     { SERVICE_HOST = "http://localhost" },
#     { SERVICE_PORT = "8080" },
#     { SERVICE_PATH = "/things" }
#   ]
# }


# data "template_file" "environment_data_json" {
#   template = file("../../src/data.json.tmpl")
#   count    = length(local.api_service_environment_values)
#   vars = {
#     name  = element(keys(local.api_service_environment_values[count.index]), 0)
#     value = element(values(local.api_service_environment_values[count.index]), 0)
#   }
# }


# # 401 Unauthorized for health check protected by authentication
# # https://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-health-checks.html
# resource "aws_lb_target_group" "api_service_target_group" {

#   health_check {
#     interval            = 60
#     path                = "/api/series"
#     port                = "traffic-port"
#     protocol            = "HTTP"
#     timeout             = 5
#     unhealthy_threshold = 2
#     healthy_threshold   = 3
#     matcher             = 401
#   }

#   port     = 8080
#   protocol = "HTTP"

#   target_type = "ip"

#   vpc_id = var.vpc_id
#   name   = format("%s-alb-tg-%s", var.api_service_name, "8080")

#   tags = merge(
#     { "Name" = format("%s-alb-tg-%s", var.api_service_name, "8080")

#       Environment  = var.environment
#       CostCenter   = var.cost_center
#       Project      = var.project
#       Owner        = var.owner
#       map-migrated = var.map-migrated
#       Deployment   = lower("Terraform")
#       Date         = formatdate("YYYY-MM-DD", timestamp())
#     },

#   )

#   depends_on = [
#     module.apps_lb
#   ]

# }



# # ECS Service and task
# module "api_service" {
#   source       = "../../modules/ecs-service"
#   environment  = var.environment
#   project      = var.project
#   cluster_name = var.cluster_name

#   namespace_id             = var.namespace_id
#   namespace_name           = var.namespace_name
#   namespace_subdomain_name = var.subdomain_name
#   service_launch_type      = "FARGATE"
#   service_platform_version = "LATEST"

#   vpc_id          = var.vpc_id
#   vpc_subnets_ids = var.vpc_private_subnets_ids

#   service_name          = var.api_service_name
#   role_policy           = templatefile("../../policies/log-stream-policy.json", { logsGroup = module.services_logs_group.logs_group_arn })
#   ecr_access_policy     = templatefile("../../policies/ecr-access-policy.json", { region = var.region, account = var.shared_services_account })
#   trust_policy          = file("../../policies/ecs-trust-policy.json")
#   execution_role_policy = templatefile("../../policies/ecs-execution-role-policy.json", { userPoolArn = module.cognito.aws_cognito_user_pool-userpool_arn })
#   task_role_policy      = templatefile("../../policies/ecs-task-role-policy.json", { userPoolArn = module.cognito.aws_cognito_user_pool-userpool_arn, sesServiceArn = var.ses_service_arn, sesTemplatesArn = var.ses_templates_arn })


#   task_network_mode = "awsvpc"

#   # TODO: send to modules: ecs-service when "publish service" is active
#   target_group_arn = aws_lb_target_group.api_service_target_group.arn

#   tasks = [
#     {
#       container_definition = templatefile("../../src/task_container_definition.json", {
#         container_name      = var.api_service_name,
#         logs_region         = var.region,
#         logs_group          = module.services_logs_group.logs_group_name,
#         stream_prefix       = var.api_service_name,
#         image               = "XXXXXXXXXXXX.dkr.ecr.eu-west-1.amazonaws.com/htcpcp-api:1.0.0.81",
#         service_environment = "${join(",", data.template_file.environment_data_json.*.rendered)}"
#         container_port      = 8080
#       })

#       name                     = var.api_service_name
#       cpu                      = 512
#       family                   = format("%s-task", var.api_service_name)
#       memory                   = 1024
#       container_name           = var.api_service_name
#       port                     = 8080
#       min_capacity             = 1
#       max_capacity             = 1
#       logs_group_arn           = module.services_logs_group.logs_group_arn
#       requires_compatibilities = ["FARGATE"]
#     }
#   ]

#   tags = {
#     Environment  = var.environment
#     CostCenter   = var.cost_center
#     Project      = var.project
#     Owner        = var.owner
#     map-migrated = var.map-migrated
#     Deployment   = lower("Terraform")
#     Date         = formatdate("YYYY-MM-DD", timestamp())
#   }


#   #   certificate_arn    = module.acm-certificate.arn
#   #   load_balancer_port = 443

#   depends_on = [
#     module.services_logs_group,
#     module.apps_lb,
#   aws_lb_target_group.api_service_target_group, ]

# }



# resource "aws_lb_listener" "api_service_listener_rule" {

#   load_balancer_arn = module.apps_lb.alb_arn
#   port              = 80
#   protocol          = "HTTP"

#   default_action {
#     target_group_arn = aws_lb_target_group.api_service_target_group.arn
#     type             = "forward"
#   }

#   tags = {
#     Environment  = var.environment
#     CostCenter   = var.cost_center
#     Project      = var.project
#     Owner        = var.owner
#     map-migrated = var.map-migrated
#     Deployment   = lower("Terraform")
#     Date         = formatdate("YYYY-MM-DD", timestamp())

#   }

#   depends_on = [module.apps_lb, aws_lb_target_group.api_service_target_group]

# }


# ####################################################################
# # API Gateway
# ####################################################################

# module "api_gateway" {
#   source          = "../../modules/api-gateway"
#   environment     = var.environment
#   project         = var.project
#   vpc_id          = var.vpc_id
#   vpc_subnets_ids = var.vpc_private_subnets_ids

#   aws_lb_listener_arn = aws_lb_listener.api_service_listener_rule.arn

#   tags = {
#     Environment  = var.environment
#     CostCenter   = var.cost_center
#     Project      = var.project
#     Owner        = var.owner
#     map-migrated = var.map-migrated
#     Deployment   = lower("Terraform")
#     Date         = formatdate("YYYY-MM-DD", timestamp())

#   }

#   depends_on = [
#     module.api_service
#   ]

# }


# # After that, initialize manually the api gateway stage
# # Create stage

# # aws --profile my_profile apigatewayv2 create-stage --region eu-west-1 --auto-deploy --api-id API_ID --stage-name '$default'




# ####################################################################
# # Outputs
# ####################################################################

# output "api_gateway_id" {
#   value = module.api_gateway.api_gateway_id
# }


