
output "external_ip_address_app" {
  value = yandex_compute_instance.app.network_interface.0.nat_ip_address
}

/*
output "external_ip_address_app" {
  value = [ for i in yandex_compute_instance.app : i.network_interface.0.nat_ip_address ]
}

output "external_ip_address_load_balancer" {
  value = [ for i in yandex_lb_network_load_balancer.reddit-lb.listener.*.external_address_spec: i ]
}
*/