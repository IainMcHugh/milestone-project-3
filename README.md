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
