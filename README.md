# omni-nucleus-stack

https://docs.omniverse.nvidia.com/nucleus/latest/enterprise/installation/install-ove-nucleus.html

## WSL

1. Modify `base_stack/nucleus-stack.env`.

2. Stand up stack.

```
cd ~
git clone https://github.com/MRIIOT/omni-nucleus-stack.git
cd omni-nucleus-stack/nucleus-stack-2023.2.7+tag-2023.2.7.gitlab.20798950.d7a79764/base_stack
sudo chmod +x generate-sample-insecure-secrets.sh
sudo ./generate-sample-insecure-secrets.sh

docker compose --env-file nucleus-stack.env -f nucleus-stack-no-ssl.yml pull
docker compose --env-file nucleus-stack.env -f nucleus-stack-no-ssl.yml up
```

## DO

1. Modify `base_stack/nucleus-stack.env`.

2. Install Docker.

```
sudo adduser omni
sudo adduser omni sudo
```

```
cd ~

curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh ./get-docker.sh

sudo groupadd docker

sudo usermod -aG docker $USER
newgrp docker
sudo systemctl enable docker
sudo systemctl start docker
```

3. Stand up stack.

```
cd ~
git clone https://github.com/MRIIOT/omni-nucleus-stack.git
cd omni-nucleus-stack/nucleus-stack-2023.2.7+tag-2023.2.7.gitlab.20798950.d7a79764/base_stack
sudo chmod +x generate-sample-insecure-secrets.sh
sudo ./generate-sample-insecure-secrets.sh

docker compose --env-file nucleus-stack.env -f nucleus-stack-no-ssl.yml pull
docker compose --env-file nucleus-stack.env -f nucleus-stack-no-ssl.yml up -d
```
