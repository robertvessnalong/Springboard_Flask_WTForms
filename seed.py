

from models import Pet, db
from app import app

db.drop_all()
db.create_all()

Pet.query.delete()

#Add Pets
petOne = Pet(name="Peter", 
             species="Dog", 
             photo_url="https://upload.wikimedia.org/wikipedia/commons/d/d0/German_Shepherd_-_DSC_0346_%2810096362833%29.jpg",
             age="3",
             notes="Friendly and Lots of Fun"
             )
petTwo = Pet(name="Bruce", 
             species="Dog", 
             photo_url="https://s3.amazonaws.com/cdn-origin-etr.akc.org/wp-content/uploads/2017/11/11234019/Bulldog-standing-in-the-grass.jpg",
             age="4",
             notes="Likes lots of naps"
             )
petThree = Pet(name="Barry", 
             species="Dog", 
             age="5",
             notes="Likes long walks",
             available=False
             )

db.session.add_all([petOne, petTwo, petThree])
db.session.commit()