# Convox API example app

Export `CONVOX_API_KEY`

## Installation

`$ pip install .`

## Docker image

`$ docker pull soulshake/py-convox`

## Usage

```
$ py-convox racks
host               id           name                                                     org                                   status                                version
-----------------  -----------  -------------------------------------------------------  ------------------------------------  ------------------------------------  ---------
demo               running      convox-demo-1485413922.us-west-2.elb.amazonaws.com       1e1077ff-d22d-43a3-a507-7d2d87267eff  ba1e701a-8097-4b0c-8503-942a41aec552
convox-production  running      convox-production-409813809.us-east-1.elb.amazonaws.com  a61bba1c-0b1b-423d-a2fb-8469d3946e42  ba1e701a-8097-4b0c-8503-942a41aec552
staging            running      convox-staging-2052606521.us-east-1.elb.amazonaws.com    128aad1b-95bb-4644-a8ed-a97bf2661863  ba1e701a-8097-4b0c-8503-942a41aec552
production         running      production-2128958833.us-east-1.elb.amazonaws.com        5e520db6-2fe2-4ced-84a5-03373db7c636  ba1e701a-8097-4b0c-8503-942a41aec552
dev                running      dev-1572861456.us-east-1.elb.amazonaws.com               f550d3c1-07b2-4335-b505-f760db4e668c  de00f038-b01d-4947-8b17-9a1784517578
cost-estimator     unreachable  cost-estimator-982785611.us-west-1.elb.amazonaws.com     8a931053-092c-434a-aa8d-31356c55369f  5b5f135f-f301-4458-a852-8777717be9a1
legit              running      legit-3122374.us-east-1.elb.amazonaws.com                26bca2da-734e-43ea-a8d0-cf573d3068cf  5b5f135f-f301-4458-a852-8777717be9a1
dev                running      dev-1572861456.us-east-1.elb.amazonaws.com               23dfda2f-d043-4e35-b254-0401aa613421  5b5f135f-f301-4458-a852-8777717be9a1
staging            running      staging-1328120697.us-east-1.elb.amazonaws.com           8f90d422-f310-464f-a132-9721a3d050f2  1baa4966-94ab-450a-acfd-3e897a0d25fa
```

```
$ docker run -e CONVOX_API_KEY -ti soulshake/py-convox racks
name               status       host                                                     id                                    organization_id                       version
-----------------  -----------  -------------------------------------------------------  ------------------------------------  ------------------------------------  ---------
demo               running      convox-demo-1485413922.us-west-2.elb.amazonaws.com       1e1077ff-d22d-43a3-a507-7d2d87267eff  ba1e701a-8097-4b0c-8503-942a41aec552
convox-production  running      convox-production-409813809.us-east-1.elb.amazonaws.com  a61bba1c-0b1b-423d-a2fb-8469d3946e42  ba1e701a-8097-4b0c-8503-942a41aec552
staging            running      convox-staging-2052606521.us-east-1.elb.amazonaws.com    128aad1b-95bb-4644-a8ed-a97bf2661863  ba1e701a-8097-4b0c-8503-942a41aec552
production         running      production-2128958833.us-east-1.elb.amazonaws.com        5e520db6-2fe2-4ced-84a5-03373db7c636  ba1e701a-8097-4b0c-8503-942a41aec552
dev                running      dev-1572861456.us-east-1.elb.amazonaws.com               f550d3c1-07b2-4335-b505-f760db4e668c  de00f038-b01d-4947-8b17-9a1784517578
cost-estimator     unreachable  cost-estimator-982785611.us-west-1.elb.amazonaws.com     8a931053-092c-434a-aa8d-31356c55369f  5b5f135f-f301-4458-a852-8777717be9a1
legit              running      legit-3122374.us-east-1.elb.amazonaws.com                26bca2da-734e-43ea-a8d0-cf573d3068cf  5b5f135f-f301-4458-a852-8777717be9a1
dev                running      dev-1572861456.us-east-1.elb.amazonaws.com               23dfda2f-d043-4e35-b254-0401aa613421  5b5f135f-f301-4458-a852-8777717be9a1
staging            running      staging-1328120697.us-east-1.elb.amazonaws.com           8f90d422-f310-464f-a132-9721a3d050f2  1baa4966-94ab-450a-acfd-3e897a0d25fa
```
