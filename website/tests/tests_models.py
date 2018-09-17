from django.test import TestCase

from website.models import Category


class CategoryModelTest(TestCase):
    """ Test case for the Category model """

    description = 'Test123'

    def test_instance(self):
        category = Category(description=self.description)
        self.assertIsInstance(category, Category)

    def test_creation(self):
        created_category = Category.objects.create(
            description=self.description
        )
        queried_category = Category.objects.get(id=created_category.id)
        self.assertEqual(created_category, queried_category)


    '''def test_str(self):
        expected_result = (
            description
        )

        call = CallRecordFactory(
            record_type='start',
            call_id=123,
            timestamp=datetime(2018, 9, 6, 20, 0, 0, tzinfo=timezone.utc)
        )
        self.assertEqual(str(call), expected_result)

    def test_repr(self):
        call = CallRecordFactory(
            record_type='end',
            call_id=123,
            timestamp=datetime(2018, 9, 6, 20, 0, 0, tzinfo=timezone.utc),
        )

        expected_result = (
            'CallRecord(call_id={}, record_type={}, timestamp={}, source={},'
            ' destination={})'.format(
                call.call_id,
                call.record_type,
                call.timestamp,
                call.source,
                call.destination
            )
        )

        self.assertEqual(repr(call), expected_result)'''
