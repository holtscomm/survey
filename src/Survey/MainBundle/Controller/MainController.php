<?php
namespace Survey\MainBundle\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\Controller;

class MainController extends Controller
{
    public function indexAction()
    {
        return $this->render(
            'SurveyMainBundle:Main:index.html.twig'
        );
    }
}