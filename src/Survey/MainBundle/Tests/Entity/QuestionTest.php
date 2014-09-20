<?php
namespace Survey\MainBundle\Tests\Entity;

use Survey\MainBundle\Entity\Question;

class QuestionTest extends \PHPUnit_Framework_TestCase
{
    public function setUp()
    {
        $this->good_category = "hea";
        $this->bad_category = "some bogus thing";
        $this->question = new Question();
    }

    public function test_succesful_creation()
    {
        $this->question->setText("This question has text! Huzzah!");
        $this->question->setCategory($this->good_category);

        $this->assertEquals($this->good_category, $this->question->getCategory());
    }

    /**
     * @expectedException DomainException
     */
    public function test_bogus_category_not_saved()
    {
        $this->question->setText("This question has text! Huzzah!");
        $this->question->setCategory($this->bad_category);

        $this->assertNull($this->question->getCategory());
    }

    public function test_getPrettyCategory_returns_correct_category_text()
    {
        $correct_category_text = "Healing";

        $this->question->setText("This question has text! Huzzah!");
        $this->question->setCategory($this->good_category);

        $this->assertEquals($correct_category_text, $this->question->getPrettyCategory());
    }

    public function test_isValidCategory_returns_true_for_valid_category()
    {
        $this->assertTrue($this->question->isValidCategory($this->good_category));
    }

    public function test_isValidCategory_returns_false_for_invalid_category()
    {
        $this->assertFalse($this->question->isValidCategory($this->bad_category));
    }
}
