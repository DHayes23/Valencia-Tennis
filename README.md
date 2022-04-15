# **Valencia Tennis Club - Code Institute Milestone 4 Project**
# **Introduction**

## **Milestone Project 4** by Denis Hayes
---
* This project has been developed to fulfil the requirements of the Code Institute's Milestone Project 4.
* This website's primary goal is to facilitate the operations of a tennis club, allowing users to manage their membership online.
* This website uses the Django full stack framework, and as such, different functional 'Apps' exist within the website.

---
## Live Website Access
---
Access the live website at: 

---
 ## **The Five Planes of UX Design**
 ---
 * This Readme is divided into different sections, with each section referring to one of the Five Planes of UX Design. 
 * Some of the topics within each of the 5 sections unavoidably cross over into other planes. 
 * Where a topic escapes the remit of the Five Planes, it will be included at the end of the document in the section called 'Appedix'.

---
 ## **Table of Contents**
---

# **Strategy** 
 ## **The Aims of the Project**
 ---
* The primary aim of the project is to provide users with means to purchase a club membership, and then manage their membership online.
* One secondary aim of the site is to allow users to book courts, reserving them for use at a specific time. 
* Another secondary aim of the site is to allow users to join tournaments created by Admins. 
---
## **User Stories**
---
### **First Time User**
* As a first time user I wish to be informed about Valencia Tennis Club and the services that it offers. This is achieved through the contents of the 'Info Section' on the home page. 
* As a first time user I may wish to join the tennis club.
* The first time user is invited to join the club in the 'Info Section' and is thereafter presented with the 'Membership' section.
* The 'Membership Section' presents the first time user with several membership options, which can be selected to progress the user to the account creation stage.
* A first time user is able to create an account using the 'Sign Up' template and form.
* Should the first time user feel that they need more information about the club, or wish to visit the club in person, the 'Contact Section' provides an email address and the club's location. 

### **Returning User**
* As a user who has already created an account I wish to be able to easily access the site's content.
* As a returning user I should be able to see and edit my personal information.
* As a returning user I should be able to see any relevant information about my membership, any court bookings that I've made and any tournaments I have entered.
* The returning user can log into the site using the 'Log In' navigation link.
* Once logged in, the user is redirected to their 'Profile' which displays all relevant information in the 'Profile Display'. The information shown in the display can be changed by clicking on a different category, navigated using the 'Profile Sidebar'.
* The returning user can view upcoming fixtures(tournaments) by navigating to the 'Fixtures Display'. The user can join the tournament by clicking the 'Join' button, if they match the criteria. 

### **Administrative User**
* As an Administrator it is important to me that I have the all the functionalities available to standard users while also having access to the tools required to properly manaage the website.
* As an Administrator, I should have access to the site's database and be able to easily edit information as needed. This is achieved using Django's built in Admin features.
* As an Administrator, I should be able to create a new tournament, and select the requirements for admission to that tournament. 
---
# **Scope** 
 ## **Existing Features**
 The following section details the existing features of the site, in their current implementation.
 ---
 ---
 ## **Existing Features - Base**
 * The following features are present on all site templates, as every template extends from base.html.
 ---
### **Favicon**
* The Favicon is a small image of a tennis ball. The favicon is brightly coloured and has a distinct connection to the purpose of the site.
### **Header**
* The Header is present at all times when accessing the website, even as the user scrolls to the bottom of a template.
* The Header displays the brand name, Valencia Tennis, prominently at all times. The brand name functions as a secondary 'Home' navigation link.
* The Header displays a dynamic navigation menu, which serves as a user's primary method of moving to different templates within the site. These items change depending on whether the user is logged in or not. 
* The Header's navigation links are replaced with a 'burger menu' icon on small screens. Clicking on this icon opens a sidenav which contains the same link elements as would be found on a large screen, displayed vertically.
### **Footer**
* The Footer, like the Header, is present at all times when accessing the website. Unlike the Header, the Footer is only visible when the user reaches the end of a template. Depending on a template's contents, the Footer may be immediately visible or may only be visible after scrolling.
---
 ## **Existing Features - Index**
* This is the landing template for any user that visits the site for the first time.
 ---
### **Info Section**
