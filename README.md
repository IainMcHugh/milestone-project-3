<h1 align="center">Milestone Project 3 - Web App Store</h1>

[View the live project here.](https://web-app-store.herokuapp.com/)

![WebApp Store](https://github.com/IainMcHugh/milestone-project-3/blob/main/static/images/mockup.png?raw=true)

Welcome to the Web App Store! The inspiration for this website came from the idea of bridging mobile apps and websites. Websites are generally viewed by consumers as functional products with apps being more appreciated for their visuals, whereas we know that websites, like apps, have huge focuses on aesthetics and visuals and we want to represent this. Feel free to browse the website's here like candy in a shop! If you've created your own website, make sure to make an account and add it to the collection here. You must include a screenshot and you can link to your site from here.

## User Experience (UX)

- ### User stories

  - #### Site Visitor Goals

    1. As a site visitor, I want to be able to browse websites by topic instead of what best matches my search query on a search engine.
    2. As a site visitor, I want to be able to have a single place that I can leave feedback and report bugs on websites I use.
    3. As a site visitor, I want to be able to view websites categorised by user ratings.
    4. As a site visitor, I want to be able to read release notes for updates to websites that I use continuously.
    5. As a returning user, I want to be able to update information on website as it changes over time.
    6. As a returning user, I want to be able to delete a website entry if the website no longer exists.

- ### Design
  - #### Colour Scheme
    - For this project I decided to maintain the styles entirely myself, for experience as well as site efficiency. In order to keep a consistent colour scheme, I made use of CSS variables which I stuck to as my colour palette for the site. Here are the colours I used:
      - ![#ffffff](https://via.placeholder.com/15/ffffff/000000?text=+) `#ffffff`
      - ![#fefefe](https://via.placeholder.com/15/fefefe/000000?text=+) `#fefefe`
      - ![#e1f1ff](https://via.placeholder.com/15/E1F1FF/000000?text=+) `#E1F1FF`
      - ![#e9e9e9](https://via.placeholder.com/15/e9e9e9/000000?text=+) `#e9e9e9`
      - ![#c4c4c4](https://via.placeholder.com/15/c4c4c4/000000?text=+) `#c4c4c4`
      - ![#11bdf3](https://via.placeholder.com/15/11bdf3/000000?text=+) `#11bdf3`
      - ![#71b7d0cc](https://via.placeholder.com/15/71b7d0cc/000000?text=+) `#71b7d0cc`
      - ![#49d5ff](https://via.placeholder.com/15/49d5ff/000000?text=+) `#49d5ff`
      - ![#71d0a0cc](https://via.placeholder.com/15/71d0a0cc/000000?text=+) `#71d0a0cc`
      - ![#d07171cc](https://via.placeholder.com/15/d07171cc/000000?text=+) `#d07171cc`
      - ![#6d6d6d](https://via.placeholder.com/15/6d6d6d/000000?text=+) `#6d6d6d`
      - ![#000000](https://via.placeholder.com/15/000000/000000?text=+) `#000000`
  - #### Typography
    - The Roboto font is the font used throughout the whole website with Sans Serif as the fallback font in case for any reason the font isn't being imported into the site correctly. I have always associated Roboto with high performance applications that aim to provide premium levels of efficiency and user experience. The readability of this font is excellent and fits well with the structured nature of the site.
      <a href="https://fonts.google.com/specimen/Roboto">Roboto</a> - Google Fonts
  - #### Imagery
    - Being a full stack application, I wanted the user's of the site to be able to drive the visual experience, and so the template foundations of the site are minimalistic but very intentional. I adamantely stuck to a google-like spacing system using either multiples of 2's or 8's across the site. I integrated cloudinary hosting to the website for imagery associated with each website, and the homepage has a Netflix like flow to it, with horizontally overflowing cards with website screenshots.
  - ### Animation
    - As I strived for a more minimalistic style to this site, there was little room for dynamic parts. I did however add subtle animation to the site logo, that uses a cubic-bezier resulting a bouncy feeling and overall adds to the sites responsive nature.

* ### Wireframes

  - Figma Wireframe - [View](https://www.figma.com/file/Wp53CDl5Ljzn83ykMjByPD/WebApp-Store?node-id=0%3A1)

## Features

- Responsive layout for all screen sizes.

- Authentication with both logging in and registering as a new user.

- Carousel based homepage displaying websites by categories.

- The ability to create, update, and delete sites.

- Information modal for overview of the sites purpose.

- Fully functional commenting with bug reporting, ratings, and most recent maintenance updates.

- 3rd party image hosting (image deleted on site removal for maximum efficiency).

- Custom Error page to maximise user's experience.

## Technologies Used

### Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://en.wikipedia.org/wiki/Python)

### Frameworks, Libraries & Programs Used

1. [Google Fonts:](https://fonts.google.com/)
   - Google fonts were used to import the 'Poppins' font into the style.css file which is used on all pages throughout the project.
2. [Font Awesome:](https://fontawesome.com/)
   - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
3. [jQuery:](https://jquery.com/)
   - jQuery came with Bootstrap to make the navbar responsive but was also used for the smooth scroll function in JavaScript.
4. [GitHub:](https://github.com/)
   - GitHub is used to store the projects code after being pushed from Git.
5. [Photoshop:](https://www.adobe.com/ie/products/photoshop.html)
   - Photoshop was used to edit the logo, resizing images and editing photos for the website.
6. [Figma:](https://figma.com/)
   - Figma was used to create the [wireframes](https://github.com/) during the design process.
7. [Visual Studio Code:](https://visualstudio.com/)
   - VSCode was the IDE I used to create, update, and maintain this project.

## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

- [W3C Markup Validator](https://validator.w3.org/) - PASS (NOTE: I had to test each HTML section manually as the validator can not handle Jinja templating)
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](https://jigsaw.w3.org/css-validator/validator?uri=http%3A%2F%2Fweb-app-store.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
  (Note:
  - The following error may show `Property backdrop-filter doesn't exist : blur(4px)`, however this is a valid css property that is available in up to date versions of most modern browsers - see [caniuse backdrop-filter](https://caniuse.com/?search=backdrop-filter)
  - You may also see warnings with regards to CSS color variables I used, again these are valid and available in up to date versions of all modern browsers - see [caniuse css-variables](https://caniuse.com/css-variables))

### Testing User Stories from User Experience (UX) Section

- #### Site Visitor Goals

  1. As a site visitor, I want to be able to browse websites by topic instead of what best matches my search query on a search engine.

     1. When a user visits the WebAppStore, they are presented with carousels of images of websites where they can choose based on how a site looks.

  2. As a site visitor, I want to be able to have a single place that I can leave feedback and report bugs on websites I use.

     1. Users can click onto or search for any website that has been added to the WebAppStore, and can leave multiple comments against that website.
     2. The user can also report any bugs found in the comments section, and these are distinguished by a red left border.

  3. As a site visitor, I want to be able to view websites categorised by user ratings.

     1. One of the 3 sections of the homepage is a 'Most popular' carousel of websites available on the site. This displays websites by order of star rating in descending order, so users can see the most popular sites.

  4. As a site visitor, I want to be able to read release notes for updates to websites that I use continuously.

     1. Website creators can simply add their own websites to their profile, which are then public. As the website owner they have the unique ability to add an 'Update' comment. This comment is distinguished by a green left border, and the most recent update by the website owner is displayed in the top panel for a website page.

  5. As a returning visitor, I want to be able to update information on website as it changes over time.

     1. On a users page, they can see a list of their websites they have added. There is an option to edit an existing website. Here they can update the name, URL, and description of the site. Clicking the update button will automatically redirect them to the updated website details page.

  6. As a returning visitor, I want to be able to delete a website entry if the website no longer exists.

     1. On a users page, they can see a list of their websites they have added. Along with the ability to edit an existing website, there is also an option to delete. If they choose to delete, then the website is removed, and can no longer be accessed.

### Further Testing

- The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
- The website was viewed on a variety of devices such as Desktop, Laptop, iPhone7, iPhone 8 & iPhoneX.
- A large amount of testing was done to ensure that all pages were linking correctly.
- Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.
- Multiple accounts were created and all of the sites functionality was tested, from CRUD operations to star rating system.

### Known Bugs

- When creating the search index I wanted users to be able to search by website as well as copying and pasting website URLs into the search bar for searching. While the search by name is working a s intended, searching by website URL returns all websites. This is most likely due to all URLs having very similar structures and with no spaces can be quite hard to get an accurate search result. To fix this I would investigate further the options available when creating a MongoDB search query, and possibly use a regex filter on the URL before performing the search query.

- The ratings bar on a website details page functions perfectly, however I found it extremely difficult to customize the range input to match my designs. While I could have found a not so elegant way to cheat this issue with CSS, I felt it would maximise SEO by sticking to a ranged input slider. The ratings bar always displays, even though it's value is only captured when the user is leaving a comment. I would fix this by adding an event listener to the dropdown and use css to hide it when the option is not Comment.

- While I added comprehensive checks to make sure duplicate websites can not be added (URL and site name must be unique in the database), technically users can add subdirectory pages of an existing website and they will be added. This is a hard fix as some websites are so large that subdirectories warrant their own page on WebAppStore.

## Future Features

- Verification over site ownership so the true site owner is the only one that can leave updates on a website.

- The ability for bug reports to notify the site owner. I would use a mailing service such as EmailJS here.

- More categories on the homepage for greater versatility.

- Tags associated with websites, which would greatly help with further categorization of websites.

## Deployment

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/IainMcHugh/milestone-project-3)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/IainMcHugh/milestone-project-3/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone git@github.com:IainMcHugh/milestone-project-3.git
```

7. Press Enter. Your local clone will be created.

```
$ git clone git@github.com:IainMcHugh/milestone-project-3.git
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

### Connecting to MongoDB

#### Requirements

You will need the following installed in order to run this project locally:

- [PIP](https://pip.pypa.io/en/stable/installing/)
- [Python 3](https://www.python.org/downloads/)

#### Steps

1. Log in to your MongoDB account.
2. Create a project called `webapp-store`.
3. Full documentation on how to setup a MongoDB cluster [here](https://docs.atlas.mongodb.com/)
4. Navigate to the `webapp-store` project, and with the Clusters tab active, choose the connect option.

![MongoDB Connect](https://github.com/IainMcHugh/milestone-project-3/blob/main/static/images/mongodb_connect_1.png?raw=true)

3. From here, select `Connect your application`.

![MongoDB Connect](https://github.com/IainMcHugh/milestone-project-3/blob/main/static/images/mongodb_connect_2.png?raw=true)

4. Copy the connection string.
5. Create a `.env.py` file in the root directory of your project.
6. In here you will need to define the following environment variables:

```python
import os

os.environ.setdefault('IP', '0.0.0.0')
os.environ.setdefault('PORT', '5000')
os.environ.setdefault('SECRET_KEY', '') # ADD YOUR SECRET KEY HERE
os.environ.setdefault('MONGO_URI', '') # ADD THE CONNECTION STRING HERE
os.environ.setdefault('MONGO_DBNAME', 'webAppStoreDB') # THE NAME OF YOUR CLUSTER'S DATABASE
```

7. The next step is to connect to cloudinary, start by visting their site [here](https://www.cloudinary.com) and logging in.
8. From the main dashboard page, you will see values associated with your `Account Details`, we need to update the `.env.py` with these:

```python
# Cloudinary
os.environ.setdefault('CLOUD_NAME', '') # ADD (Account Details > Cloud name) HERE
os.environ.setdefault('CLOUD_KEY', '') # ADD (Account Details > API Key) HERE
os.environ.setdefault('CLOUD_SECRET', '') # (ADD Account Details > API Secret) HERE
os.environ.setdefault('CLOUD_ENV', '') # ADD (Account Details > API Environment variable) HERE
```

9. Open the terminal in the root directory and run the following:

```
pip install -r requirements.txt
```

10. You should now be able to run the application locally, to start:

```
<Cloudinary API ENV VAR> python3 app.py
```

You will need to replace `<Cloudinary API ENV VAR>` with your entire cloudinary API environment variable string.
The application should be running locally on:

```
http://0.0.0.0:5000/
```

### Deployment to Heroku

The first step is to create a `requirements.txt` and Procfile in the root directory of the project, which can be done with the following:

```
   pip3 freeze --local > requirements.txt
   echo web: python3 app.py > Procfile
```

#### Deployment

1. Navigate to [Heroku](https://www.heroku.com) and sign in.
2. Create a new application, giving it an appropriate name and region.
3. By default you should be now on the application dashboard page, navigate to the `Deploy` tab and `Connect to Github`

![Connect to Github](https://github.com/IainMcHugh/milestone-project-3/blob/main/static/images/heroku_connect_1.png?raw=true)

4. You will need to connect your project's Github repository by entering the `repo-name` and selecting `Connect`.
5. When your project is successfully connected, navigate to the `Settings` tab and select `Reveal Config Vars`

![Reveal Config Vars](https://github.com/IainMcHugh/milestone-project-3/blob/main/static/images/heroku_connect_2.png?raw=true)

6. Here you will need to add the following config variables:

![Add Config Vars](https://github.com/IainMcHugh/milestone-project-3/blob/main/static/images/heroku_connect_3.png?raw=true)

NOTE: These should be identical to the environment variables defined in your `.env.py` file. The only additional value is the `CLOUDINARY_URL`, which should have the same value as your `CLOUD_ENV` variable.

7. Navigate back to the `Deploy` tab, and under `Automatic deploys` you will need to select `Enable Automatic Deploys`.
8. Make sure that the master/main branch is selected, when successful it should appear like this:

![Successful Auto Deploy](https://github.com/IainMcHugh/milestone-project-3/blob/main/static/images/heroku_connect_4.png?raw=true)

9. You should now be able to open the application by selecting the `Open app` along the top.

### Database Structure

I used TypeScript interfaces to create the structures for how I wanted my MongoDB documents and collections to be formed. I would greatly recommend this as it helped me mentally map what I would need to create each page. Here are the structures I used:

```typescript
type UserWebsite = {
    website_id: websiteObjectId();
    isOwner: boolean;
}

type Comments = {
  username: string;
  timestamp: Date;
  value: string;
  comment_type: 'COMMENT' | 'BUG' | 'UPDATE';
};

interface Users {
  username: string;
  email: string;
  websites: UserWebsite[];
}

interface Websites {
  objectId: objectId();
  owners: string[];
  title: string;
  url: string;
  description: string;
  stars: number;
  reviews: number;
  last_update: string;
  comments: Comments[];
}
```

## Credits

### Code

- [CSS scollbar](https://developer.mozilla.org/en-US/docs/Web/CSS/::-webkit-scrollbar): This helped me a lot when trying to customise the scrollbar within the text area on the message panel, which was a vital requirement within the design.

- [Article by Valentino Gagliardi](https://www.valentinog.com/blog/link-download/): This extremely helpful method allowed me to embed the entire JSON chat logs within an anchor tag's href attribute, making it downloadable by the user.

### Content

- All content was written by Iain McHugh.

- [Multi-mockup](https://techsini.com/multi-mockup/): A great resource for generating mockup displays for the site on various different screens and devices. Used for the cover photo of this readme file.

- Star icon: https://fontawesome.com/
- delete flash message: https://stackoverflow.com/questions/57660542/flask-closing-flash-message
- bounce effect on logo: https://stackoverflow.com/questions/29786230/how-to-create-css3-bounce-effect
- Cloud docs: https://cloudinary.com/documentation/image_upload_api_reference#sample_response
  https://cloudinary.com/documentation/django_integration
  https://github.com/tiagocordeiro/flask-cloudinary
- Slider: https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_rangeslider
- Sorting in Jinja templating: https://stackoverflow.com/questions/1959386/how-do-you-sort-a-list-in-jinja2

### Media

- All images were created/edited by the developer or sourced from image websites where Creative Commons license is active.

- [Site for icons](https://www.flaticon.com/)
- [The Rubber Duck image source](https://www.pngegg.com/en/png-zmwpv)

### Acknowledgements

- I would like to thank my mentor, Oluwafemi. With each mentoring session I feel I am learning more and more about how to approach web projects, and much of this is down to your guidance. I definitely feel that following your advice has allowed me to acheive a high quality in my projects thus far.

- I also want to thank Code Institute in providing me with information and guides on how to structure my project. There is always new things for me to learn with JavaScript and I have loved every minute of the course content.

- Again I would like to thank the Slack community associated with Code Institute. It is a great way to find inspiration and feel as part of a community who share a similar mindset and goal.

note: in env.py change key

MY NOTES (DELETE AFTER)

Sample upload cloudinary

Sample Data:

https://www.facebook.com/
Facebook is an American online social media and social networking service based in Menlo Park, California, and a flagship service of the namesake company Facebook, Inc. It was founded by Mark Zuckerberg, along with fellow Harvard College students and roommates Eduardo Saverin, Andrew McCollum, Dustin Moskovitz, and Chris Hughes.

https://github.com/
GitHub, Inc. is a provider of Internet hosting for software development and version control using Git. It offers the distributed version control and source code management (SCM) functionality of Git, plus its own features. It provides access control and several collaboration features such as bug tracking, feature requests, task management, continuous integration and wikis for every project. Headquartered in California, it has been a subsidiary of Microsoft since 2018.

https://www.figma.com/
Figma is a vector graphics editor and prototyping tool which is primarily web-based, with additional offline features enabled by desktop applications for macOS and Windows. The Figma Mirror companion apps for Android and iOS allow viewing Figma prototypes on mobile devices. The feature set of Figma focuses on use in user interface and user experience design, with an emphasis on real-time collaboration.

https://www.youtube.com/
YouTube is an American online video-sharing platform headquartered in San Bruno, California. The service, created in February 2005 by three former PayPal employees—Chad Hurley, Steve Chen, and Jawed Karim—was bought by Google in November 2006 for US$1.65 billion and now operates as one of the company's subsidiaries. YouTube is the second most-visited website after Google Search, according to Alexa Internet rankings.

https://www.linkedin.com
LinkedIn is an American business and employment-oriented online service that operates via websites and mobile apps. Launched on May 5, 2003, the platform is mainly used for professional networking, and allows job seekers to post their CVs and employers to post jobs. As of 2015, most of the company's revenue came from selling access to information about its members to recruiters and sales professionals. Since December 2016, it has been a wholly owned subsidiary of Microsoft. As of February 2021, LinkedIn had 740 million registered members from 150 countries.

https://www.netflix.com
Netflix, Inc. is an American over-the-top content platform and production company headquartered in Los Gatos, California. Netflix was founded in 1997 by Reed Hastings and Marc Randolph in Scotts Valley, California. The company's primary business is a subscription-based streaming service offering online streaming from a library of films and television series, including those produced in-house. In January 2021, Netflix reached 203.7 million subscribers, including 73 million in the United States.

https://stackoverflow.com/
Stack Overflow is a question and answer site for professional and enthusiast programmers. It is a privately held website, the flagship site of the Stack Exchange Network, created in 2008 by Jeff Atwood and Joel Spolsky. It features questions and answers on a wide range of topics in computer programming.

https://trello.com
Trello is a web-based, Kanban-style, list-making application and is a subsidiary of Atlassian. Originally created by Fog Creek Software in 2011, it was spun out to form the basis of a separate company in 2014 and later sold to Atlassian in January 2017. The company is based in New York City.

https://mail.google.com
Gmail is a free email service developed by Google. Users can access Gmail on the web and using third-party programs that synchronize email content through POP or IMAP protocols. Gmail started as a limited beta release on April 1, 2004 and ended its testing phase on July 7, 2009. By October 2019, Gmail had 1.5 billion active users worldwide.

https://twitter.com
Twitter is an American microblogging and social networking service on which users post and interact with messages known as "tweets". Registered users can post, like and retweet tweets, but unregistered users can only read them. Users access Twitter through its website interface or its mobile-device application software ("app"), though the service could also be accessed via SMS before April 2020.

https://www.zalando.com
Zalando SE is a German multi national e-commerce company based in Berlin, Germany. The company follows a platform approach, offering fashion and lifestyle products to customers in 17 European markets. Zalando was founded in Germany in 2008.The Swedish company Kinnevik is Zalando's largest stakeholder, with a 21% share.

CLOUDINARY_URL=cloudinary://483728613595827:VyZwK4orRoyA79PJUGYH2f8pdII@dp6r73isa python3 app.py
