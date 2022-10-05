 
The Code regarding the navigation bar was taken from this site https://medium.com/@ukaohachizoba6/how-to-build-a-responsive-navigation-bar-using-html-css-and-javascript-330ee12ff686
and written by Ukaoha Chizoba
<nav class="nav">
                <ul class="nav-links">
                  <li class="nav-item"><a href="index.html">Home</a></li>
                  <li class="nav-item"><a href="AboutMe.html"> About</a></li>
                  <li class="nav-item"><a href="Projects.html">Projects</a></li>
                  <li class="nav-item"><a href="ContactMe.html">Contact Me</a></li>
                </ul>

  .nav .nav-links{
    margin-top: 10%;
    display: flex;
    justify-content: space-around;
    align-items: center;
    width: 100%;
    padding: 0.5rem 3rem;
  }
   
  .nav li{
    padding: 1rem;
   list-style-type: none;
  }
 
  .nav a{
    text-decoration: none;
    color: rgb(211,211,211);
    cursor: pointer;
    font-size: 1rem;
    margin-left: 1rem;
    font-weight: 500;
  }

The code for the media Queries was written by Josh Byers from https://www.studiopress.com/website-respond-mobile-devices/

@media only screen
and (min-device-width : 320px)
and (max-device-width : 480px)
 {
    
}


@media only screen
and (min-device-width : 768px)
and (max-device-width : 1024px) {
}


@media only screen
and (min-width : 1224px) {
}