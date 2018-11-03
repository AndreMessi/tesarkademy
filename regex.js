function isAcceptedUsername(username) {
    var Regex = /^[aiueo]{3}[a-z0-9]{2,7}$/i ;
    return Regex.test(username) ;
}
// Cara menggunakan fungsi di atas
if (isAcceptedUsername("aaat3st1ng")) {
    alert("Username Is Valid") ;
} else {
    alert("Username Is Invalid") ;
}
