// Fetch prints the content found at a URL.
package main
import (
"fmt"
//"io/ioutil"
"net/http"
"os"
"io"
"strings"
)

func main() {
	for _, url := range os.Args[1:] {
		if ! strings.HasPrefix(url, "http://") {
			url = "http://" + url
		} 
		resp, err := http.Get(url)
		if err != nil {
			fmt.Fprintf(os.Stderr, "fetch: %v\n", err)
			os.Exit(1)
		}
		//b, err := ioutil.ReadAll(resp.Body)
		b, err := io.Copy(os.Stdout, resp.Body)
		//c := resp.Status
		resp.Body.Close()
		if err != nil {
			fmt.Fprintf(os.Stderr, "fetch: reading %s: %v\n", url, err)
			os.Exit(1)
		}
	fmt.Printf("%s\n", b)
	//fmt.Printf("%s HTTP status = \n", resp.Status)
	} 
	
}
