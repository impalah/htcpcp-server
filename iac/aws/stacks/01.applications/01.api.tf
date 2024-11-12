# ####################################################################
# # Application configuration
# ####################################################################

module "htcpcp-api" {
  source           = "../../modules/lambda"
  environment      = var.environment
  project          = var.project
  function_name    = "htcpcp-api"
  function_memory  = "2048"
  function_storage = "512"
  function_timeout = "300"
  image            = var.image
  env_variables = {
    LOGGER_NAME                                = "htcpcp.Engine"
    LOG_LEVEL                                  = "DEBUG"
    AUTH_MIDDLEWARE_DISABLED                   = "true"
    AUTH_MIDDLEWARE_LOG_LEVEL                  = "DEBUG"
    AUTH_PROVIDER_AWS_COGNITO_USER_POOL_ID     = "eu-west-1_NZLzZP1xc"
    AUTH_PROVIDER_AWS_COGNITO_USER_POOL_REGION = "eu-west-1"
    OTEL_ENABLED                               = "false"
    OTEL_SERVICE_NAME                          = "htcpcp"
    OTEL_EXPORTER_OTLP_ENDPOINT                = "http://localhost:4317"
    COFFEE_POT_ID                              = "1234567890"
    COFFEE_POT_NAME                            = "MyCoffeePot"
    COFFEE_POT_LOCATION                        = "OfficeKitchen"
    COFFEE_POT_TEAPOT                          = "false"
  }

  #   vpc_id          = module.vpc.vpc_id
  #   vpc_subnets_ids = values(module.vpc.private_subnet_ids)

  depends_on = [
    module.cognito
  ]

}



####################################################################
# API Gateway
####################################################################

module "api_gateway" {
  source               = "../../modules/api-gateway"
  environment          = var.environment
  project              = var.project
  lambda_function_arn  = module.htcpcp-api.function_arn
  lambda_function_name = module.htcpcp-api.function_name
  # vpc_id          = var.vpc_id
  # vpc_subnets_ids = var.vpc_private_subnets_ids

  # aws_lb_listener_arn = aws_lb_listener.api_service_listener_rule.arn


  depends_on = [
    module.htcpcp-api
  ]

}


# After that, initialize manually the api gateway stage
# Create stage

# aws --profile my_profile apigatewayv2 create-stage --region eu-west-1 --auto-deploy --api-id API_ID --stage-name '$default'




# ####################################################################
# # Outputs
# ####################################################################

output "api_gateway_id" {
  value = module.api_gateway.api_gateway_id
}


