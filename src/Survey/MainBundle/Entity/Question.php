<?php
namespace Survey\MainBundle\Entity;

use Doctrine\ORM\Mapping as ORM;
use DomainException;

/**
 * @ORM\Entity
 * @ORM\Table(name="question")
 */
class Question
{
    private $category_mappings = array(
        "adm" => "Administration (Leadership)",
        "apo" => "Apostleship (Missionary)",
        "cou" => "Counsellor (Exhorter)",
        "dis" => "Discernment",
        "eva" => "Evangelist",
        "fai" => "Faith",
        "giv" => "Giving",
        "hea" => "Healing",
        "int" => "Interpretation of Tongues",
        "kno" => "Knowledge",
        "mir" => "Miracles",
        "pro" => "Prophecy (Preacher/Proclaimer)",
        "she" => "Sheperding (Pastor/Teacher)",
        "ser" => "Serving (Helps)",
        "sho" => "Showing Mercy (Compassion)",
        "tea" => "Teaching",
        "ton" => "Tongues",
        "wis" => "Wisdom"
    );

    private $answer_choices = array(
        1 => "Almost always true of me",
        2 => "Sometimes/Occasionally true of me",
        3 => "Rarely if at all true of me"
    );

    /**
     * @ORM\Column(type="integer")
     * @ORM\Id
     * @ORM\GeneratedValue(strategy="AUTO")
     */
    protected $id;

    /**
     * @ORM\Column(type="string", length=300)
     */
    protected $text;

    /**
     * @ORM\Column(type="string", length=3)
     */
    protected $category;

    /**
     * Get id
     *
     * @return integer 
     */
    public function getId()
    {
        return $this->id;
    }

    /**
     * Set text
     *
     * @param string $text
     * @return Question
     */
    public function setText($text)
    {
        $this->text = $text;

        return $this;
    }

    /**
     * Get text
     *
     * @return string 
     */
    public function getText()
    {
        return $this->text;
    }

    /**
     * Set category. If it is not a valid category, DomainException will be
     *  thrown
     *
     * @param string $category
     * @return Question
     * @throws DomainException
     */
    public function setCategory($category)
    {
        if($this->isValidCategory($category))
        {
            $this->category = $category;
        }
        else
        {
            throw new DomainException("Category " . $category . " is not a valid category");
        }

        return $this;
    }

    /**
     * Get category
     *
     * @return string 
     */
    public function getCategory()
    {
        return $this->category;
    }

    /**
     * Get the expanded version of a category, i.e. "hea" becomes "Healing"
     * 
     * @return string
     */
    public function getPrettyCategory()
    {
        $pretty_category = "";
        if($this->isValidCategory($this->getCategory()))
        {
            $pretty_category = $this->category_mappings[$this->getCategory()];
        }
        return $pretty_category;
    }

    /**
     * Checks if the category passed in is valid
     * 
     * @return boolean
     */
    public function isValidCategory($category)
    {
        return array_key_exists($category, $this->category_mappings);
    }

    /**
     * Get the answer choices for every question (it is always the same three choices)
     * 
     * @return array of strings
     */
    public function getAnswerChoices()
    {
        return $this->answer_choices;
    }
}
