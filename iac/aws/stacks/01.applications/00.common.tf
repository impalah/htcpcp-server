#################################################################
# VPC and subnets
#################################################################




#################################################################
# Log group
#################################################################

# module "services_logs_group" {
#   source           = "../../modules/cloudwatch"
#   environment      = var.environment
#   project          = var.project
#   log_group_prefix = var.log_group_prefix
#   log_group_name   = var.log_group_name

#   tags = {
#     Environment = var.environment
#     CostCenter  = var.cost_center
#     Project     = var.project
#     Owner       = var.owner
#     Deployment  = lower("Terraform")
#     Date        = formatdate("YYYY-MM-DD", timestamp())
#   }

# }

#################################################################
# Cognito
#################################################################

module "cognito" {
  source                     = "../../modules/cognito"
  environment                = var.environment
  project                    = var.project
  userpool_name              = var.user_pool_name
  userpool_domain            = format("%s-%s", lower(var.environment), lower(var.project))
  resource_server_identifier = format("%s-%s-rsid", lower(var.environment), lower(var.project))
  resource_server_name       = format("%s-%s-rs", lower(var.environment), lower(var.project))
  groups                     = var.user_pool_groups
  resource_server_scopes     = var.resource_server_scopes
  api_client_users           = var.api_client_users
  client_callback_urls       = ["http://localhost:4200"]

  tags = {
    Environment = var.environment
    CostCenter  = var.cost_center
    Project     = var.project
    Owner       = var.owner
    Deployment  = lower("Terraform")
    Date        = formatdate("YYYY-MM-DD", timestamp())
  }

}

