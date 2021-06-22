terraform {
/* required_providers {
     yandex = {
       source = "yandex-cloud/yandex"
     }
   }
*/
  backend "s3" {
    endpoint   = "storage.yandexcloud.net"
    bucket     = "emilmind"
    region     = "ru-central1"
    key        = "terraform.tfstate"
    access_key = "access_key"
    secret_key = "secret_key"

    skip_region_validation      = true
    skip_credentials_validation = true
  }
}
