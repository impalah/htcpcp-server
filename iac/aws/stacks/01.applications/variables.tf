
# The home of the variables
variable "tags" {
  description = "External tags map"
  type        = map(string)
  default     = {}
}

variable "region" {
  description = "Set the primary region"
  type        = string
  default     = "eu-west-2"
}

variable "environment" {
  description = "Set environment name"
  type        = string
  default     = ""
}

variable "customer" {
  description = "Set customer name"
  type        = string
  default     = ""
}

variable "cost_center" {
  description = "Cost center associated with the project"
  type        = string
  default     = ""
}

variable "project" {
  description = "Project name"
  type        = string
  default     = ""
}

variable "organization" {
  description = "Organization name (internal)"
  type        = string
  default     = ""
}

variable "map-migrated" {
  description = "Map migrated"
  type        = string
  default     = ""
}

variable "bu-code" {
  description = "Business unit code"
  type        = string
  default     = ""
}

variable "owner" {
  description = "Owner name (internal)"
  type        = string
  default     = ""
}


variable "shared_services_account" {
  description = "Shared services account"
  type        = string
  default     = null
}


# variable "aws_kms_ssm_default_key" {
#   description = "Default key that protects my SSM parameters when no other key is defined (aws kms describe-key --key-id alias/aws/ssm --region region )"
#   type        = string
#   default     = null
# }

variable "vpc_id" {
  description = "Id for the VPC"
  type        = string
  default     = ""
}

variable "vpc_public_subnets_ids" {
  description = "Public subnets"
  type        = set(string)
  default     = []
}

variable "vpc_private_subnets_ids" {
  description = "Private subnets"
  type        = set(string)
  default     = []
}

variable "vpc_db_private_subnets_ids" {
  description = "Private DB subnets"
  type        = set(string)
  default     = []
}

# Frontend
variable "frontend_bucket_name" {
  description = "Bucket name"
  type        = string
  default     = null
}


variable "user_pool_name" {
  description = "User pool name"
  type        = string
  default     = null
}

variable "user_pool_groups" {
  description = "User pool groups"
  type        = list(string)
  default     = []
}

variable "user_pool_client_name" {
  description = "User pool client name"
  type        = string
  default     = null
}

variable "user_pool_client_secret" {
  description = "User pool client secret"
  type        = string
  default     = null
}

variable "user_pool_domain" {
  description = "User pool domain"
  type        = string
  default     = null
}

variable "resource_server_scopes" {
  description = "A list of scopes for API users"
  type = list(object({
    name        = string
    description = string
  }))
  default = [
    {
      name        = "administrator"
      description = "Default scope for users"
    }
  ]
}

variable "api_client_users" {
  description = "A list of API client users for machine to machine communication"
  type = list(object({
    name   = string
    scopes = list(string)
  }))
  default = [
    {
      name   = "admin"
      scopes = ["administrator"]
    }
  ]
}


variable "api_service_name" {
  description = "Service name"
  type        = string
  default     = null
}


variable "cluster_name" {
  description = "Name of the ECS cluster"
  type        = string
  default     = null
}

variable "namespace_id" {
  description = "Namespace ID"
  type        = string
  default     = null
}

variable "namespace_name" {
  description = "Namespace name"
  type        = string
  default     = null
}

variable "subdomain_name" {
  description = "Subdomain name"
  type        = string
  default     = null
}



variable "networking_account" {
  description = "ID of the networking account (for creating ALB target groups)"
  type        = string
  default     = null
}

variable "ec2_key_pair_path" {
  description = "EC2 key pair path"
  type        = string
  default     = null
}

variable "ec2_user" {
  description = "EC2 user"
  type        = string
  default     = "ec2-user"
}

variable "alb_base_listener_priority" {
  description = "Base priority for the ALB listener rules"
  type        = number
  default     = 100
}

# ECS Cluster configuration
variable "ecs_cluster_name" {
  description = "ECS cluster name"
  type        = string
  default     = null
}

variable "efs_mount_path" {
  description = "Mount path for the EFS (for building)"
  type        = string
  default     = "/mnt/efs"
}

variable "ecs_mount_base_path" {
  description = "Base path for mounting the WFS folder on containers"
  type        = string
  default     = "ci"
}


variable "efs_trigger_active" {
  description = "Only create the folder structure if the EFS is created"
  type        = bool
  default     = true
}

variable "task_definition_family" {
  description = "Task definition family"
  type        = string
  default     = null
}



# Frontend

variable "frontend_s3_endpoint" {
  description = "S3 endpoint"
  type        = string
  default     = null
}


variable "frontend_origin_id" {
  description = "Distribution origin ID"
  type        = string
  default     = null
}


# Backend bucket name
variable "backend_bucket_name" {
  description = "Backend Bucket name"
  type        = string
  default     = null
}


# Certificate for Cloudfront
variable "cdn_certificate_arn" {
  description = "TLS certificate arn for Cloudfront"
  type        = string
  default     = null
}

variable "cdn_frontend_domains" {
  description = "Domains for Cloudfront"
  type        = list(string)
  default     = []
}




variable "nginx_container_image" {
  description = "NGINX Task container image"
  type        = string
  default     = null
}

variable "api_container_image" {
  description = "API Task container image"
  type        = string
  default     = null
}

variable "websocket_container_image" {
  description = "Websocket API Task container image"
  type        = string
  default     = null
}

variable "cron_container_image" {
  description = "Cron Task container image"
  type        = string
  default     = null
}

variable "log_group_prefix" {
  description = "Service Log group prefix"
  type        = string
  default     = null
}

variable "log_group_name" {
  description = "Service Log group name"
  type        = string
  default     = null
}

variable "read_database_secret_id" {
  description = "Read database secret ID"
  type        = string
  default     = null
}


variable "write_database_secret_id" {
  description = "Write database secret ID"
  type        = string
  default     = null
}



variable "elasticache_cluster_id" {
  description = "ElastiCache cluster ID"
  type        = string
  default     = null
}



variable "database_name" {
  description = "Name for the RDS database"
  type        = string
  default     = null
}

variable "database_username" {
  description = "Username for the RDS database"
  type        = string
  default     = null
}

variable "database_password" {
  description = "Password for the RDS database"
  type        = string
  default     = null
}

variable "database_azs" {
  description = "Availability zones for the RDS database"
  type        = list(string)
  default     = null
}

variable "database_instance_name" {
  description = "RDS database"
  type        = string
  default     = null
}

variable "database_engine" {
  description = "RDS database"
  type        = string
  default     = null
}

variable "database_engine_version" {
  description = "RDS database"
  type        = string
  default     = null
}

variable "database_instance_class" {
  description = "RDS database"
  type        = string
  default     = null
}


variable "database_port" {
  description = "Database port"
  type        = number
  default     = 3306
}



variable "backend_configuration_name" {
  description = "Backend secret name"
  type        = string
  default     = null
}

variable "backend_configuration_value" {
  description = "Backend secret value (provisional)"
  type        = string
  default     = null
}

variable "aurora_min_capacity" {
  description = "Minimum capacity for the cluster"
  type        = number
  default     = 1
}

variable "aurora_max_capacity" {
  description = "Maximum capacity for the cluster"
  type        = number
  default     = 10
}


variable "api_min_capacity" {
  description = "Minimum capacity for the cluster"
  type        = number
  default     = 1
}

variable "api_max_capacity" {
  description = "Maximum capacity for the cluster"
  type        = number
  default     = 10
}

variable "ws_min_capacity" {
  description = "Minimum capacity for the cluster"
  type        = number
  default     = 1
}

variable "ws_max_capacity" {
  description = "Maximum capacity for the cluster"
  type        = number
  default     = 10
}

variable "api_path" {
  description = "API path"
  type        = string
  default     = "/*"
}

variable "ws_path" {
  description = "WS path"
  type        = string
  default     = "/app/local*"
}




variable "oauth_public_key" {
  description = "OAuth Key"
  type        = string
  default     = null
}

variable "oauth_private_key" {
  description = "OAuth Key"
  type        = string
  default     = null
}

variable "frontend_configuration_name" {
  description = "Frontend secret name"
  type        = string
  default     = null
}

variable "myhtg_configuration_name" {
  description = "MyHtg secret name"
  type        = string
  default     = null
}

variable "apiconnect_configuration_name" {
  description = "API Connect secret name"
  type        = string
  default     = null
}


variable "database_type" {
  description = "The type of database to use (aurora, rds)"
  type        = string
  default     = "aurora"
}

variable "alb_service_name" {
  description = "Application load balancer Service name"
  type        = string
  default     = null
}

variable "alb_listener_port" {
  description = "Application load balancer listener port"
  type        = number
  default     = 80
}

variable "alb_listener_protocol" {
  description = "Application load balancer listener protocol"
  type        = string
  default     = "HTTP"
}


variable "http_port" {
  description = "Http port"
  type        = number
  default     = 80
}

variable "ses_email_host" {
  description = "SES email host"
  type        = string
  default     = null
}

variable "ses_email_port" {
  description = "SES email port"
  type        = number
  default     = 587
}

variable "ses_email_display_name" {
  description = "SES email display name"
  type        = string
  default     = null
}

variable "ses_email_sender_email" {
  description = "SES email sender email"
  type        = string
  default     = null
}

variable "ses_email_identity_arn" {
  description = "SES email identity ARN"
  type        = string
  default     = null
}

variable "ses_email_confirmation_base_url" {
  description = "SES email confirmation base URL"
  type        = string
  default     = null
}

variable "ses_email_roberlo" {
  description = "SES email roberlo"
  type        = string
  default     = null
}

variable "ses_email_username" {
  description = "SES email username"
  type        = string
  default     = null
}

variable "ses_email_password" {
  description = "SES email password"
  type        = string
  default     = null
}

variable "ses_service_arn" {
  description = "SES service ARN"
  type        = string
  default     = null
}

variable "ses_templates_arn" {
  description = "SES templates ARN"
  type        = string
  default     = null
}



