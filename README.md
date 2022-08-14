# Team108-DatasyncRepo

A project that allows users compare multiples excel files easily.

<!-- landing page html -->
<nav>
      <ul class="nav">
        <li class="logo">
          <a href="#"></a><img src="images/logo.svg" alt="" />
        </li>
        <li class="item"><a href="index.html">Home</a></li>
        <li class="item"><a href="#">Features</a></li>
        <li class="item"><a href="#">How to use</a></li>
        <li class="button sec"><a href="login.html">Sign In</a></li>
        <li class="button reg"><a href="signup.html">Register now</a></li>
      </ul>
    </nav>

<!-- landing page css -->

.nav {
background-color: rgb(212, 200, 212);
padding: 5px 20px;
display: flex;
flex-wrap: wrap;
justify-content: space-between;
align-items: center;
height: 90%;
}
ul {
list-style: none;
}
a {
text-decoration: none;
}
.item a:hover {
text-decoration: underline;
}

.nav li {
font-size: 16px;
/_ padding: 15px 5px; _/
}
.nav li a {
display: block;
}
nav .sec a {
color: #ce1949;
}
nav .item a {
color: #ce1949;
}

.logo a {
font-size: 20px;
width: 10%;
margin-left: 10%;
}

.button a {
text-decoration: none;
color: white;
padding: 15px 25px;
background: linear-gradient(85.8deg, #81365f -15.76%, #ce1949 73.17%);
border: 2px solid #ce1949;
border-radius: 4px;
}
.button.sec a {
background: transparent;
}
.button a:hover {
background: rgb(184, 183, 183);
border-color: rgb(184, 183, 183);
transition: all 0.25s;
opacity: 1px;
}

<!-- footer html-->
<footer>
      <div class="content">
        <div class="footer-logo"></div>

        <div class="links-boxes">
          <ul class="box">
            <li class="logo">
              <img src="images/logo.svg" alt="contact logo" />
            </li>
            <li><a href="#">Mission statement</a></li>
          </ul>
          <ul class="box">
            <li><a href="index.html">Home</a></li>
            <li><a href="#">Docs</a></li>
            <li><a href="#">About us</a></li>
          </ul>
          <ul class="box">
            <li><a href="#">Product</a></li>
            <li><a href="#">Life display</a></li>
            <li><a href="#">Consultations</a></li>
          </ul>
          <ul class="box">
            <li><a href="#">Contact us</a></li>
            <li><a href="#">Services</a></li>
            <li><a href="#">Widgetkit</a></li>
          </ul>
        </div>
      </div>
      <hr />

      <div class="social">
        <a href="#"
          ><img src="images/entypo-social_facebook-with-circle.svg" alt=""
        /></a>
        <a href="#"><img src="images/et_linkedin.svg" alt="" /></a>
        <a href="#"><img src="images/et_twitter.svg" alt="" /></a>
      </div>

      <div class="copyright"><p>&copy; Copyright. All rights reserved.</p></div>
    </footer>

    <!-- footer css -->
    footer {

padding-top: 40px;
background: var(--blue);
width: 100%;
bottom: 0;
left: 0px;
height: 400px;
}

footer .content {
max-width: 1250px;
margin: auto;
padding: 20px 30px 30px 20px;
}

footer .content .links-boxes {
width: 100%;
display: flex;
justify-content: space-between;
color: white;
}
footer .content .links-boxes .box {
width: calc(100% / 5 - 10px);
}

footer .content .links-boxes .box li {
margin: 6px 0;
list-style: none;
}

footer .content .links-boxes .box li a {
color: white;
font: 24px;
font-weight: 500;
text-decoration: none;
transition: all 0.4s ease;
}

footer .content .links-boxes .box li a:hover {
opacity: 1;
text-decoration: underline;
}
hr {
width: 90%;
border: 0;
border-bottom: 1px solid #ccc;
margin: 10px auto;
}

footer .media-icon {
font-size: 30px;
align-self: flex-start;
}

footer .social {
width: 100%;
margin: 0 auto;
text-align: center;
padding: 10px;
}

.copyright {
color: white;
font-size: 12px;
width: 100%;
margin: 0 auto;
text-align: center;
padding: 20px;
}

<!-- dashboard navhtml -->
<header class="main-header">
      <div class="main-logo">
        <img src="/images/logo.svg" alt="" />
      </div>
      <nav class="header-nav">
        <ul class="nav-group">
          <li><a href="dashboard.html">Home</a></li>
          <li><a href="singleFile.html">Compare</a></li>
          <li><a href="convert.html">Convert</a></li>
          <li><a href="library.html">Files Library</a></li>
        </ul>
      </nav>
      <div class="user-group">
        <button><a href="#">FAQ</a></button>
        <i class="fa-regular fa-bell"></i>
      </div>
    </header>

 <!-- dashboard navcss -->

    .main-header {

width: 100%;
height: 80px;
background-color: rgb(212, 200, 212);
padding: 10px 2px;
display: flex;
justify-content: space-between;
align-items: center;
}
.main-logo {
width: 10%;
size: 20px;
margin-left: 3%;
}
.header-nav {
width: 40%;
margin-left: 0px;
}
.nav-group {
display: flex;
margin-left: 0px;
}
.nav-group li {
list-style: none;
align-items: center;
justify-content: center;
}
.nav-group li a {
text-decoration: none;
font-size: 16px;
color: #ce1949;
margin-right: 30px;
}
.nav-group li a:hover {
text-decoration: underline;
}

.user-group {
width: 30%;
margin-top: 10px;
}
.user-group button {
width: 15%;
height: 40px;
align-items: center;
border: 2px solid rgb(119, 118, 119);
background-color: rgb(212, 200, 212);
border-radius: 2px;
}
.user-group a {
color: rgb(119, 118, 119);
text-decoration: none;
font-weight: 600;
}
