FROM amazonlinux:2023

# Update base system
RUN dnf upgrade -y

# Install core dev tools
RUN dnf install -y \
    git \
    make \
    tar \
    gzip \
    unzip \
    gcc \
    gcc-c++ \
    python3 \
    python3-pip

# Install Node.js (LTS 18 using NodeSource)
RUN curl -fsSL https://rpm.nodesource.com/setup_18.x | bash - && \
    dnf install -y nodejs

# Install AWS CLI v2
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "/awscliv2.zip" && \
    unzip /awscliv2.zip -d / && \
    /aws/install && \
    rm -rf /aws /awscliv2.zip

# Set working directory (mounted at runtime)
WORKDIR /workspace

# How to Use This Dev Environment
    # docker compose build
    # docker compose run dev
