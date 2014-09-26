<?php
namespace Survey\UserBundle;

use Symfony\Component\HttpKernel\Bundle\Bundle;

class SurveyUserBundle extends Bundle
{
    public function getParent()
    {
        return "FOSUserBundle";
    }
}