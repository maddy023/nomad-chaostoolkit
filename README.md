<h1 align="center">Welcome to nomad-chaostoolkit 👋</h1>
<p>
  <a href="#" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
</p>

> Designed to bring chaos engineering principles to the Nomad orchestration platform. The project provides various chaos experiments that can be executed on Nomad clusters via Choastoolkit

# Features

- Terminate / Restart Random Allocations
- Drain Random Node
- Increase / Decrease Allocation Memory & CPU 

# Requirements

- [Docker](https://docs.docker.com/engine/install/ "Docker") >=20.10.0
- [Consul](https://developer.hashicorp.com/consul/docs/install "Consul") >=1.13.0 
- [Nomad](https://developer.hashicorp.com/nomad/docs/install "Nomad") >=1.5.0
- [Chaostoolkit](https://chaostoolkit.org/reference/usage/install/ "Chaostoolkit") >=1.15.1
- [python-nomad](https://github.com/jrxFive/python-nomad/ "python-nomad")

# Setup Local Environment

### Start Consul Dev
```sh
consul agent -dev
```
### Start Nomad Dev 
```sh
nomad agent -dev -bind 0.0.0.0 -log-level INFO
```

# How to run experiment?

If you dont have any nomad job, deploy demo.nomad

```sh
nomad job run -detach ./nomad/job/demo.nomad

# Check job status
nomad job status demo-webapp
```

Modify nomad_toolkit.yaml to add python modules in order which you need to run the experiments.

```sh
chaos run nomad_toolkit.yaml
```

## Author

👤 **Mhathesh**

* Github: [@maddy023](https://github.com/maddy023)
* LinkedIn: [@https:\/\/www.linkedin.com\/in\/mhathesh-tsr\/](https://linkedin.com/in/https:\/\/www.linkedin.com\/in\/mhathesh-tsr\/)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/maddy023/nomad-chaostoolkit/issues). 
