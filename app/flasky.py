from app import create_app
from app.models import Category

app = create_app('prd')

@app.context_processor
def inject_categories():
    categories = Category.get_all_objects()  # Fetch all categories here
    return {'categories': categories}


if __name__=='__main__':
    app.run()
