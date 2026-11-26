
terraform {
  required_version = ">= 1.5.0"
}

variable "project_name" {
  description = "Enterprise application name"
  type        = string
  default     = "sec-agency"
}

variable "environment" {
  description = "Deployment environment"
  type        = string
  default     = "dev"
}

variable "aws_region" {
  description = "Target AWS region"
  type        = string
  default     = "us-east-1"
}

locals {
  common_tags = {
    Project     = var.project_name
    Environment = var.environment
    ManagedBy   = "Terraform"
  }
}

output "project_name" {
  value = var.project_name
}

output "environment" {
  value = var.environment
}

output "target_region" {
  value = var.aws_region
}
