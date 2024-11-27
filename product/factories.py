import factory

from .models import Category, Product


class CategoryFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("pystr")
    slug = factory.Faker("pystr")
    description = factory.Faker("pystr")
    active = factory.Iterator([True, False])

    class Meta:
        model = Category
        skip_postgeneration_save = True


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product
        skip_postgeneration_save = True

    title = factory.Sequence(lambda n: f"Product {n}")
    price = factory.Faker("random_int", min=10, max=1000)
    active = True

    # Use o método post-generation para adicionar categorias
    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing
            return

        if extracted:
            # A list of categories were passed in
            for category in extracted:
                self.category.add(category)
