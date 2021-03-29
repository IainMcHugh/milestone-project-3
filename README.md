This is my milestone 3 project.

note: in env.py change key

Need form for adding a new page

construct edit url with unique website object id.

```typescript
type UserWebsite = {
    website_id: websiteObjectId();
    isOwner: boolean;
}

interface Users {
  username: string;
  email: string;
  websites: UserWebsite[]
}

type Comments = {
  username: string;
  timestamp: Date;
  value: string;
  comment_type: 'COMMENT' | 'BUG' | 'UPDATE';
};

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

1. Sign up and Log in - (Create Read user document)
2. As user, CRUD website - (Create Read Update Delete website/objectId for website stored against user, data stored in Website)
3. As user, add comment - (push comment to Websites comment array)

template inheritance - components

Credits

- Star icon: https://fontawesome.com/
- delete flash message: https://stackoverflow.com/questions/57660542/flask-closing-flash-message
- bounce effect on logo: https://stackoverflow.com/questions/29786230/how-to-create-css3-bounce-effect
- Cloud docs: https://cloudinary.com/documentation/image_upload_api_reference#sample_response
  https://cloudinary.com/documentation/django_integration
  https://github.com/tiagocordeiro/flask-cloudinary
- Slider: https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_rangeslider
- Sorting in Jinja templating: https://stackoverflow.com/questions/1959386/how-do-you-sort-a-list-in-jinja2

Sample upload cloudinary

- cloudinary.uploader.upload("sample.jpg",crop="limit",tags="samples",width=3000,height=2000)
- To start: CLOUDINARY_URL=cloudinary://483728613595827:VyZwK4orRoyA79PJUGYH2f8pdII@dp6r73isa python3 app.py

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
