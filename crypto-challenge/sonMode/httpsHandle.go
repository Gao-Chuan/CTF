package sonMode

import (
	"crypto/rand"
	"crypto/sha256"
	"fmt"
	"html/template"
	"io"
	"net/http"
	"reflect"
	"strconv"
	"time"
)

type Manager struct {
	firstName string
	lastName  string
	nickName  string
	password  string
	salt      []byte
	idCard    string
	gender    string
	superID   int
}

type User struct {
	firstName string
	lastName  string
	nickName  string
	password  string
	salt      []byte
	idCard    string
	gender    string
}

func errHandle(err error) {
	if err != nil {
		panic(err)
	}
}

func renderHTML(w http.ResponseWriter, r *http.Request, tmpl string, header string, locals map[string]interface{}) (err error) {
	lg := langChoose(r)
	tmpl = lg + "/" + tmpl
	header = lg + "/" + header
	t, err := template.ParseFiles("htmlFile/"+tmpl+".html", "htmlFile/public/"+header+".html")
	errHandle(err)
	err = t.Execute(w, locals)
	errHandle(err)
	return
}

func langChoose(r *http.Request) (lg string) {
	lg = r.FormValue("lang")
	if lg == "" {
		lg = "us"
	}

	return
}

func Welcome(w http.ResponseWriter, r *http.Request) {
	cookie, err := r.Cookie("NeverLandBank")
	if err != nil {
		err := renderHTML(w, r, "welcome", "visitorHeader", nil)
		errHandle(err)
		return
	}
	value := dec(key, cookie.Value)
	if value[:5] == "admin" {
		io.WriteString(w, "you got the flag! send your cookie to 1phan plz~")
	}
	switch string(value[0]) {
	case "u":
		locals := make(map[string]interface{})
		locals["username"] = "user " + value[5:]
		err := renderHTML(w, r, "welcomeSignedIn", "signedInHeader", locals)
		errHandle(err)
	case "m":
		locals := make(map[string]interface{})
		locals["username"] = "manager " + value[8:]
		err := renderHTML(w, r, "welcomeSignedIn", "signedInHeader", locals)
		errHandle(err)
	case "s":
		locals := make(map[string]interface{})
		locals["username"] = "Super manager " + value[12:]
		err := renderHTML(w, r, "welcomeSignedIn", "signedInHeader", locals)
		errHandle(err)
	default:
		err := renderHTML(w, r, "welcome", "visitorHeader", nil)
		errHandle(err)
	}
}

func SignUpHandle(w http.ResponseWriter, r *http.Request) {
	if r.Method == "GET" {
		switch r.FormValue("sort") {
		case "":
			err := renderHTML(w, r, "signUp", "signUpHeader", nil)
			errHandle(err)
		case "user":
			err := renderHTML(w, r, "userSignUp", "signUpHeader", nil)
			errHandle(err)
		case "manager":
			err := renderHTML(w, r, "managerSignUp", "signUpHeader", nil)
			errHandle(err)
		default:
			locals := make(map[string]interface{})
			locals["url"] = r.URL
			renderHTML(w, r, "404", "signUpHeader", locals)
		}
	}
	if r.Method == "POST" {
		switch r.FormValue("sort") {
		case "user":
			if r.FormValue("password") != r.FormValue("password_again") {
				io.WriteString(w, "Error! Two different passwords are entered!")
				break
			}
			user := new(User)
			user.firstName = r.FormValue("firstname")
			user.lastName = r.FormValue("lastname")
			user.nickName = r.FormValue("nickname")
			salt := make([]byte, 32)
			_, err := rand.Read(salt)
			errHandle(err)
			user.salt = salt
			temp := sha256.Sum256([]byte(r.FormValue("password") + string(salt[:32])))
			user.password = string(temp[:])
			fmt.Println(reflect.TypeOf(user.password))
			user.idCard = r.FormValue("idcard")
			if r.FormValue("gender") != "male" && r.FormValue("gender") != "female" {
				io.WriteString(w, "Hello bad girl/boy")
				break
			}
			user.gender = r.FormValue("gender")
			db := SqlDbInitHandle("webServer")
			defer db.Close()
			err = db.Ping()
			errHandle(err)
			_, err = db.Exec(
				"INSERT INTO users VALUES (NULL, ?, ?, ?, ?, ?, 0, ?, ?, 1)",
				user.nickName,
				user.firstName,
				user.lastName,
				user.password,
				user.salt,
				user.idCard,
				user.gender,
			)
			errHandle(err)
		case "manager":
			if r.FormValue("password") != r.FormValue("password_again") {
				io.WriteString(w, "Error! Two different passwords are entered!")
				break
			}
			manager := new(Manager)
			manager.firstName = r.FormValue("firstname")
			manager.lastName = r.FormValue("lastname")
			manager.nickName = r.FormValue("nickname")
			salt := make([]byte, 32)
			_, err := rand.Read(salt)
			errHandle(err)
			manager.salt = salt
			temp := sha256.Sum256([]byte(r.FormValue("password") + string(salt[:32])))
			manager.password = string(temp[:])
			manager.idCard = r.FormValue("idcard")
			if r.FormValue("gender") != "male" && r.FormValue("gender") != "female" {
				io.WriteString(w, "Hello bad girl/boy")
				break
			}
			manager.gender = r.FormValue("gender")
			tempStr := r.FormValue("superID")
			manager.superID, _ = strconv.Atoi(tempStr)
			db := SqlDbInitHandle("webServer")
			defer db.Close()
			err = db.Ping()
			errHandle(err)
			_, err = db.Exec(
				"INSERT INTO managers_temp VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)",
				manager.nickName,
				manager.firstName,
				manager.lastName,
				manager.password,
				manager.salt,
				manager.idCard,
				manager.gender,
				manager.superID,
			)
			errHandle(err)
		default:
			io.WriteString(w, "You should choose whether signing up as a user or  signing up as a manager")
		}
		err := renderHTML(w, r, "successfulSignUp", "signUpHeader", nil)
		errHandle(err)
	}
}

func setCookie(value string, w http.ResponseWriter) {
	expiration := time.Now().Add(24 * time.Hour)
	value = enc(key, value)
	cookie := http.Cookie{Name: "NeverLandBank", Value: value, Expires: expiration}
	http.SetCookie(w, &cookie)
}

func SignInHandle(w http.ResponseWriter, r *http.Request) {
	if r.Method == "GET" {
		err := renderHTML(w, r, "signIn", "signInHeader", nil)
		errHandle(err)
	}
	if r.Method == "POST" {
		userName := r.FormValue("nickname")
		passwd := r.FormValue("password")
		db := SqlDbInitHandle("webServer")
		err := db.Ping()
		errHandle(err)

		rows, err := db.Query("select password, salt from users where nickName = ?", userName)
		errHandle(err)

		for rows.Next() {
			var hashedpw string
			var salt []byte
			rows.Scan(&hashedpw, &salt)
			passwdTemp := sha256.Sum256([]byte(passwd + string(salt[:32])))
			if string(passwdTemp[:]) == hashedpw {
				setCookie("user-"+userName, w)
				locals := make(map[string]interface{})
				locals["userName"] = userName
				renderHTML(w, r, "successfulSignIn", "signInHeader", locals)
			}
			return
		}
		io.WriteString(w, "Wrong passwrd or nickname!")
	}
}

func SignOutHandle(w http.ResponseWriter, r *http.Request) {
	cookie := http.Cookie{Name: "NeverLandBank", Path: "/", MaxAge: -1}
	http.SetCookie(w, &cookie)
	io.WriteString(w, "Sign out successful! Bye~")
}
