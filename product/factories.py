import factory

from product.models import Category, Product


class CategoryFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("pystr")
    slug = factory.Faker("pystr")
    description = factory.Faker("pystr")
    active = factory.Iterator([True, False])

    class Meta:
        model = Category
        skip_postgeneration_save = True


class ProductFactory(factory.django.DjangoModelFactory):
    price = factory.Faker("pyint")
    category = factory.LazyAttribute(CategoryFactory)
    title = factory.Faker("pystr")

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for category in extracted:
                self.category.add(category)

        self.save()

    class Meta:
        model = Product
        skip_postgeneration_save = True
