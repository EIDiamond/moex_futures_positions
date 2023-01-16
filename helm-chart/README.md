## Introduction

The chart for deployment the project on a [Kubernetes](http://kubernetes.io) cluster using the [Helm](https://helm.sh) package manager.

## Install the Chart

To install the chart with the release name `moex_futures_positions` from folder `helm-chart/`:

```console
helm install moex_futures_positions helm-chart/
```

The command deploys on the Kubernetes cluster in the default configuration. The configuration section lists the parameters that can be configured during installation.

> **Tip**: List all releases using `helm list`

## Uninstall the Chart

To uninstall/delete the `moex_futures_positions` deployment:

```console
helm delete --purge moex_futures_positions
```

The command removes nearly all the Kubernetes components associated with the chart and deletes the release.

## Configuration
| Parameter                                    | Description                                                                                                               | Default |
|----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|---------|
| `env.contract`                               | futures contract name                                                                                                     | `""`    |
| `env.day`                                    | day of requesting date                                                                                                    | `0`     |
| `env.month`                                  | month of requesting date                                                                                                  | `0`     |
| `env.year`                                   | year of requesting date                                                                                                   | `0`     |
| `env.range`                                  | period of days from requesting date (can be negative or zero)                                                             | `0`     |
| `env.pg_host`                                | postgres host name                                                                                                        | `""`    |
| `env.pg_port`                                | postgres port number                                                                                                      | `5432`  |
| `env.pg_user`                                | postgres user name                                                                                                        | `""`    |
| `env.pg_password`                            | postgres user password                                                                                                    | `""`    |
| `env.pg_db`                                  | postgres db name with following [tables](https://github.com/EIDiamond/moex_futures_positions/blob/main/create_tables.sql) | `""`    |

Specify each parameter using the `--set key=value[,key=value]` argument to `helm install`. For example:

```console
$ # Helm 3
helm install moex_futures_positions helm-chart/ --set env.contract=CNY
```

Alternatively, a YAML file that specifies the values for the parameters can be
provided while installing the chart. For example:

```console
$ # Helm 3
helm install moex_futures_positions helm-chart/ -f values.yaml
```

or change the default [values.yaml](values.yaml) file. 