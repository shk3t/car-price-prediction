package utils

import "strings"

func Capitalize(str string) string {
	if len(str) == 0 {
		return str
	}
	return strings.ToUpper(str[:1]) + strings.ToLower(str[1:])
}