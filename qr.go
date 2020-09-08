package main

import (
	"fmt"
	"github.com/boombuler/barcode"
	"github.com/boombuler/barcode/qr"
	"image/png"
	"os"
)

func main() {
	args := os.Args

	path := args[1]
	code := args[2]

	generateqr(path, code)
}

func generateqr(path string, code string) {
	qrCode, _ := qr.Encode(code, qr.L, qr.Auto)
	qrCode, _ = barcode.Scale(qrCode, 512, 512)
	f, _ := os.Create(fmt.Sprintf("%s.png", path))
	png.Encode(f, qrCode)
}
