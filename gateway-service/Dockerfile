FROM golang:1.23
WORKDIR /gateway-service
RUN apt update
RUN apt install -y curl
COPY go.mod go.sum .
RUN go mod download
COPY . .
RUN go build -o build/main cmd/main.go
CMD ./build/main