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
