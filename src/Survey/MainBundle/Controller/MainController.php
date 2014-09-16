<?php
namespace Survey\MainBundle\Controller;

use Survey\MainBundle\Entity\Question;
use Symfony\Bundle\FrameworkBundle\Controller\Controller;
use Symfony\Component\HttpFoundation\Response;

class MainController extends Controller
{
    public function indexAction()
    {
        return $this->render(
            'SurveyMainBundle:Main:index.html.twig'
        );
    }

    public function createAction()
    {
        $question = new Question();
        $question->setText("This question has text! Huzzah!");
        $question->setCategory("healing");

        $em = $this->getDoctrine()->getManager();
        $em->persist($question);
        $em->flush();

        return new Response('Created new question with id '. $question->getId());
    }

    public function showAction($id)
    {
        $question = $this->getDoctrine()
            ->getRepository('SurveyMainBundle:Question')
            ->find($id);

        if(!$question)
        {
            throw $this->createNotFoundException("No question found for id ".$id);
        }

        return $this->render(
            'SurveyMainBundle:Main:index.html.twig', 
            array("question"=>$question)
        );
    }

    public function showByCategoryAction($category)
    {
        $repository = $this->getDoctrine()
            ->getRepository('SurveyMainBundle:Question');

        $questions = $repository->findBy(
            array('category' => $category)
        );

        return $this->render(
            'SurveyMainBundle:Main:index.html.twig', 
            array("questions" => $questions)
        );
    }
}