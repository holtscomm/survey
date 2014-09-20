<?php
namespace Survey\MainBundle\Controller;

use Survey\MainBundle\Entity\Question;
use Symfony\Bundle\FrameworkBundle\Controller\Controller;
use Symfony\Component\HttpFoundation\Response;

class MigrationController extends Controller
{
    public function confirmAction()
    {
        return $this->render(
            'SurveyMainBundle:Migration:confirm.html.twig'
        );
    }

    public function migrateAction()
    {
        // Get the database manager
        $em = $this->getDoctrine()->getManager();

        $question1 = new Question();
        $question1->setText("I work best under moderate or heavy pressure.");
        $question1->setCategory("adm");
        $em->persist($question1);

        $question2 = new Question();
        $question2->setText("I tend to emerge as the leader of whatever.");
        $question2->setCategory("adm");
        $em->persist($question2);

        $question3 = new Question();
        $question3->setText("I feel I could learn another language well in order to minister to those in a different culture.");
        $question3->setCategory("apo");
        $em->persist($question3);

        $question4 = new Question();
        $question4->setText("I feel I could proclaim the Gospel in a new area and see a new group of Christians formed.");
        $question4->setCategory("apo");
        $em->persist($question4);

        $question5 = new Question();
        $question5->setText("People seek me out for counsel and guidance.");
        $question5->setCategory("cou");
        $em->persist($question5);

        $question6 = new Question();
        $question6->setText("I can identify with the faltering in such a way as to encourage them to renew their hope and commitments.");
        $question6->setCategory("cou");
        $em->persist($question6);

        $question7 = new Question();
        $question7->setText("I can readily see the difference between truth and error.");
        $question7->setCategory("dis");
        $em->persist($question7);

        $question8 = new Question();
        $question8->setText("I have an ability to differentiate between the evil and the good.");
        $question8->setCategory("dis");
        $em->persist($question8);

        $question9 = new Question();
        $question9->setText("I share how Christ has brought me to Himself in a way that seems meaningful to non-believers.");
        $question9->setCategory("eva");
        $em->persist($question9);

        $question10 = new Question();
        $question10->setText("When I am asked to speak or in conversation I desire to speak messages which are primarily the gospel of salvation.");
        $question10->setCategory("eva");
        $em->persist($question10);

        $question11 = new Question();
        $question11->setText("I lose track of time when I am praying for other people.");
        $question11->setCategory("fai");
        $em->persist($question11);

        $question12 = new Question();
        $question12->setText("I believe God will keep His promises in spite of circumstances.");
        $question12->setCategory("fai");
        $em->persist($question12);

        $question13 = new Question();
        $question13->setText("I believe that God has given me a special ability both to make and to share money.");
        $question13->setCategory("giv");
        $em->persist($question13);

        $question14 = new Question();
        $question14->setText("God has enabled me to give money and I love to give liberally to Christian causes.");
        $question14->setCategory("giv");
        $em->persist($question14);

        $question15 = new Question();
        $question15->setText("I have been used by God to impart health to people who are spiritually, emotionally or physically sick.");
        $question15->setCategory("hea");
        $em->persist($question15);

        $question16 = new Question();
        $question16->setText("I have a burden to pray for and help those who need healing.");
        $question16->setCategory("hea");
        $em->persist($question16);

        $question17 = new Question();
        $question17->setText("I desire to use my capacity to translate tongues into understandable words.");
        $question17->setCategory("int");
        $em->persist($question17);

        $question18 = new Question();
        $question18->setText("I sense an inner impulse to communicate to others what a speaker in tongues has said.");
        $question18->setCategory("int");
        $em->persist($question18);

        $question19 = new Question();
        $question19->setText("I find myself discovering new truths from the Bible.");
        $question19->setCategory("kno");
        $em->persist($question19);

        $question20 = new Question();
        $question20->setText("I have confidence that the insights I possess and share will bring changes in attitude and conviction to my fellow Christians.");
        $question20->setCategory("kno");
        $em->persist($question20);

        $question21 = new Question();
        $question21->setText("I am able to discern when to delegate important responsibilities, and to whom.");
        $question21->setCategory("adm");
        $em->persist($question21);

        $question22 = new Question();
        $question22->setText("I enjoy planning and administrating programs which benefit Christians and non-Christians.");
        $question22->setCategory("adm");
        $em->persist($question22);

        $question23 = new Question();
        $question23->setText("I have been able to relate well to Christians of a different race, language, and culture.");
        $question23->setCategory("apo");
        $em->persist($question23);

        $question24 = new Question();
        $question24->setText("I have an unquenchable desire to be sent out by this church to start new churches.");
        $question24->setCategory("apo");
        $em->persist($question24);

        $question25 = new Question();
        $question25->setText("I enjoy helping others work out detailed steps for becoming better Christian disciples.");
        $question25->setCategory("cou");
        $em->persist($question25);

        $question26 = new Question();
        $question26->setText("People will take correction from me because they know I'm on their side.");
        $question26->setCategory("cou");
        $em->persist($question26);

        $question27 = new Question();
        $question27->setText("I am able to identify ideas, plans or activities that are not true to the Bible.");
        $question27->setCategory("dis");
        $em->persist($question27);

        $question28 = new Question();
        $question28->setText("My \"hunches\" concerning people are almost always accurate when tested over time.");
        $question28->setCategory("dis");
        $em->persist($question28);

        $question29 = new Question();
        $question29->setText("I have a burden to seek out unbelievers in order to win them to Christ.");
        $question29->setCategory("eva");
        $em->persist($question29);

        $question30 = new Question();
        $question30->setText("Some people think my witnessing tactics are pushy but I am not.");
        $question30->setCategory("eva");
        $em->persist($question30);

        $question31 = new Question();
        $question31->setText("I have a deep conviction of the reality of our active God in the daily affairs of my local church.");
        $question31->setCategory("fai");
        $em->persist($question31);

        $question32 = new Question();
        $question32->setText("I take prayer requests very seriously and pray until the answer comes.");
        $question32->setCategory("fai");
        $em->persist($question32);

        $question33 = new Question();
        $question33->setText("I sense that some appeals for money are not worthy appeals.");
        $question33->setCategory("giv");
        $em->persist($question33);

        $question34 = new Question();
        $question34->setText("I have a burden for world missions and for the ministry of this local church.");
        $question34->setCategory("giv");
        $em->persist($question34);

        $question35 = new Question();
        $question35->setText("I have seen God heal someone in direct answer to my prayers.");
        $question35->setCategory("hea");
        $em->persist($question35);

        $question36 = new Question();
        $question36->setText("I believe that God has used me to heal another person and that God was glorified through this event.");
        $question36->setCategory("hea");
        $em->persist($question36);

        $question37 = new Question();
        $question37->setText("I have interpreted messages given in tongues so as to help others worship God without confusion.");
        $question37->setCategory("int");
        $em->persist($question37);

        $question38 = new Question();
        $question38->setText("I have interpreted tongues in a way that seemed to help both believers and non-Christians.");
        $question38->setCategory("int");
        $em->persist($question38);

        $question39 = new Question();
        $question39->setText("I am very happy when acquiring and mastering new facts and principles which can be applied to given situations to aid others in their growth and stability.");
        $question39->setCategory("kno");
        $em->persist($question39);

        $question40 = new Question();
        $question40->setText("I enjoy reading and studying a great deal in order to build myself up in the understanding of biblical truths.");
        $question40->setCategory("kno");
        $em->persist($question40);

        $question41 = new Question();
        $question41->setText("I willingly bear the responsibility for the success and failure of a group or organization.");
        $question41->setCategory("adm");
        $em->persist($question41);

        $question42 = new Question();
        $question42->setText("People look to me for guidance in organizing and managing.");
        $question42->setCategory("adm");
        $em->persist($question42);

        $question43 = new Question();
        $question43->setText("More than most, I have a strong desire to see peoples beyond this particular church and city won to the Lord.");
        $question43->setCategory("apo");
        $em->persist($question43);

        $question44 = new Question();
        $question44->setText("I generally have short term relationships with people because I want to meet more non-Christians, see them become strong Christians then go on to some other new people.");
        $question44->setCategory("apo");
        $em->persist($question44);

        $question45 = new Question();
        $question45->setText("I have the ability to motivate others to faith and good works.");
        $question45->setCategory("cou");
        $em->persist($question45);

        $question46 = new Question();
        $question46->setText("I have urged others to seek Biblical solutions to their affliction or suffering.");
        $question46->setCategory("cou");
        $em->persist($question46);

        $question47 = new Question();
        $question47->setText("I sense a great deal of uneasiness with people, facts or situations which are later shown to be false, wrong or evil.");
        $question47->setCategory("dis");
        $em->persist($question47);

        $question48 = new Question();
        $question48->setText("I have accurately recognized whether teaching is from God, from an evil spirit or of human origin.");
        $question48->setCategory("dis");
        $em->persist($question48);

        $question49 = new Question();
        $question49->setText("I would rather witness than do anything else.");
        $question49->setCategory("eva");
        $em->persist($question49);

        $question50 = new Question();
        $question50->setText("I am disappointed when non-Christians are not given an invitation to accept Christ at the end of worship service.");
        $question50->setCategory("eva");
        $em->persist($question50);

        $question51 = new Question();
        $question51->setText("I have the capacity to believe and expect great things from God.");
        $question51->setCategory("fai");
        $em->persist($question51);

        $question52 = new Question();
        $question52->setText("I am confident that God will bring victory into difficult situations even when others are discouraged.");
        $question52->setCategory("fai");
        $em->persist($question52);

        $question53 = new Question();
        $question53->setText("When I give, I don't want anyone else to know about it. Yet I realize that I can inspire others by the liberality of heart that God has given me.");
        $question53->setCategory("giv");
        $em->persist($question53);

        $question54 = new Question();
        $question54->setText("I am sensitive to the financial and material needs of others.");
        $question54->setCategory("giv");
        $em->persist($question54);

        $question55 = new Question();
        $question55->setText("Sometimes God has given me a special faith to pray for His direct intervention to bring health to some afflicted person.");
        $question55->setCategory("hea");
        $em->persist($question55);

        $question56 = new Question();
        $question56->setText("I have seen God use me in helping people who have been hurt by others.");
        $question56->setCategory("hea");
        $em->persist($question56);

        $question57 = new Question();
        $question57->setText("I know whether or not the gift of tongues is being exercised in proper order and according to scriptures.");
        $question57->setCategory("int");
        $em->persist($question57);

        $question58 = new Question();
        $question58->setText("I seem to know if the persons speaking in tongues is from God or not.");
        $question58->setCategory("int");
        $em->persist($question58);

        $question59 = new Question();
        $question59->setText("I have the ability to research and locate principles of truth from \"jungles of facts.\"");
        $question59->setCategory("kno");
        $em->persist($question59);

        $question60 = new Question();
        $question60->setText("I am able to arrange and analyse helpful biblical and secular facts.");
        $question60->setCategory("kno");
        $em->persist($question60);

        $question61 = new Question();
        $question61->setText("I am willing to make decisions even at the risk of being misunderstood by others.");
        $question61->setCategory("adm");
        $em->persist($question61);

        $question62 = new Question();
        $question62->setText("I can organize church resources for an effective ministry.");
        $question62->setCategory("adm");
        $em->persist($question62);

        $question63 = new Question();
        $question63->setText("I can adapt to different lifestyles so as to establish a christian witness in a culture different than mine.");
        $question63->setCategory("apo");
        $em->persist($question63);

        $question64 = new Question();
        $question64->setText("I think that I may be called to take the gospel to a completely unchurched area.");
        $question64->setCategory("apo");
        $em->persist($question64);

        $question65 = new Question();
        $question65->setText("I have a compelling desire to effectively counsel the perplexed, the guilty or the addicted.");
        $question65->setCategory("cou");
        $em->persist($question65);

        $question66 = new Question();
        $question66->setText("I have the real burden to show people how scripture relates to personal conduct and the resolution of problems.");
        $question66->setCategory("cou");
        $em->persist($question66);

        $question67 = new Question();
        $question67->setText("I can see through people who wear masks before most other people pick up on it.");
        $question67->setCategory("dis");
        $em->persist($question67);

        $question68 = new Question();
        $question68->setText("I can detect spiritual phoniness before most others can.");
        $question68->setCategory("dis");
        $em->persist($question68);

        $question69 = new Question();
        $question69->setText("I think God has given me the gift of evangelism.");
        $question69->setCategory("eva");
        $em->persist($question69);

        $question70 = new Question();
        $question70->setText("Leading other people to a decision for salvation through faith is something I've experienced.");
        $question70->setCategory("eva");
        $em->persist($question70);

        $question71 = new Question();
        $question71->setText("I find that circumstances or situations don't keep me from being ever confident in the all sufficiency of Jesus Christ. .");
        $question71->setCategory("fai");
        $em->persist($question71);

        $question72 = new Question();
        $question72->setText("I think if ... God said it then I believe it, that settles it, let's get on with it.");
        $question72->setCategory("fai");
        $em->persist($question72);

        $question73 = new Question();
        $question73->setText("I am ready, able, and willing to give if a valid need exists.");
        $question73->setCategory("giv");
        $em->persist($question73);

        $question74 = new Question();
        $question74->setText("Other people may tend to think I am materialistic because of the importance I put on money, but I am not.");
        $question74->setCategory("giv");
        $em->persist($question74);

        $question75 = new Question();
        $question75->setText("I believe that God has often used me to reconcile people who are at odds with God or others.");
        $question75->setCategory("hea");
        $em->persist($question75);

        $question76 = new Question();
        $question76->setText("Some people have told me they think I have the gift of healing.");
        $question76->setCategory("hea");
        $em->persist($question76);

        $question77 = new Question();
        $question77->setText("God has given me a special ability to translate messages from speakers of other languages into that of hearers.");
        $question77->setCategory("int");
        $em->persist($question77);

        $question78 = new Question();
        $question78->setText("I have full control over the gift of interpretation so that it is used in an orderly fashion.");
        $question78->setCategory("int");
        $em->persist($question78);

        $question79 = new Question();
        $question79->setText("I seem to be able to remember or access facts and resources more readily than most people.");
        $question79->setCategory("kno");
        $em->persist($question79);

        $question80 = new Question();
        $question80->setText("I have had the experience of knowing something even though no one told me.");
        $question80->setCategory("kno");
        $em->persist($question80);

        $question81 = new Question();
        $question81->setText("I can lead others in matters of planning and in deploying the abilities of the group.");
        $question81->setCategory("adm");
        $em->persist($question81);

        $question82 = new Question();
        $question82->setText("I can see the total picture easier than some others, and can use my insights to give guidance.");
        $question82->setCategory("adm");
        $em->persist($question82);

        $question83 = new Question();
        $question83->setText("I am intrigued with the idea of moving into another culture to learn their ways so as to win them to Christ.");
        $question83->setCategory("apo");
        $em->persist($question83);

        $question84 = new Question();
        $question84->setText("I feel confident even when I am standing alone for Christ in a hostile, non-Christian environment.");
        $question84->setCategory("apo");
        $em->persist($question84);

        $question85 = new Question();
        $question85->setText("I desparately want people to make biblical decisions that will honor God and cause them to grow in Christ.");
        $question85->setCategory("cou");
        $em->persist($question85);

        $question86 = new Question();
        $question86->setText("I have found that when I sing or speak people are motivated to faith and good deeds.");
        $question86->setCategory("cou");
        $em->persist($question86);

        $question87 = new Question();
        $question87->setText("God has used me to warn others of the danger of a certain teaching.");
        $question87->setCategory("dis");
        $em->persist($question87);

        $question88 = new Question();
        $question88->setText("I can identify elements of truth or error when I hear or read the teachings of others.");
        $question88->setCategory("dis");
        $em->persist($question88);

        $question89 = new Question();
        $question89->setText("I enjoy seeking out unbelievers in order to win them to Christ.");
        $question89->setCategory("eva");
        $em->persist($question89);

        $question90 = new Question();
        $question90->setText("I believe that everyone in the church should be involved in evangelism but it seems that I have by God's grace a high proportion of people that I share with actually come to Christ.");
        $question90->setCategory("eva");
        $em->persist($question90);

        $question91 = new Question();
        $question91->setText("I have received an unusual assurance from God that He will do the impossible.");
        $question91->setCategory("fai");
        $em->persist($question91);

        $question92 = new Question();
        $question92->setText("Others have told me that I have great faith.");
        $question92->setCategory("fai");
        $em->persist($question92);

        $question93 = new Question();
        $question93->setText("I feel deeply moved when confronted with urgent financial needs in God's work.");
        $question93->setCategory("giv");
        $em->persist($question93);

        $question94 = new Question();
        $question94->setText("I would be willing to maintain a lower standard of living in order to benefit God's work.");
        $question94->setCategory("giv");
        $em->persist($question94);

        $question95 = new Question();
        $question95->setText("I often pray with or for others that their pain will be removed.");
        $question95->setCategory("hea");
        $em->persist($question95);

        $question96 = new Question();
        $question96->setText("I often have a strong sense that God wants to heal a particular person.");
        $question96->setCategory("hea");
        $em->persist($question96);

        $question97 = new Question();
        $question97->setText("I have been told by Godly and mature Christian leaders that I have the gift of interpretation of tongues.");
        $question97->setCategory("int");
        $em->persist($question97);

        $question98 = new Question();
        $question98->setText("My interpretations always agree with the truth of Scripture.");
        $question98->setCategory("int");
        $em->persist($question98);

        $question99 = new Question();
        $question99->setText("Often God has helped me solve a problem even though others were not aware that there was a problem.");
        $question99->setCategory("kno");
        $em->persist($question99);

        $question100 = new Question();
        $question100->setText("My great desire is to use Bible knowledge in ministering to the needs of other believers.");
        $question100->setCategory("kno");
        $em->persist($question100);

        $question101 = new Question();
        $question101->setText("I have experienced God using me to perform a powerful act that could be seen as altering the ordinary course of nature.");
        $question101->setCategory("mir");
        $em->persist($question101);

        $question102 = new Question();
        $question102->setText("I have been able to glorify God by miraculously changing circumstances through the name of the Lord.");
        $question102->setCategory("mir");
        $em->persist($question102);

        $question103 = new Question();
        $question103->setText("I am willing to assume a long-term personal responsibility for the spiritual welfare for a group of believers.");
        $question103->setCategory("she");
        $em->persist($question103);

        $question104 = new Question();
        $question104->setText("I am more relationship oriented than task oriented.");
        $question104->setCategory("she");
        $em->persist($question104);

        $question105 = new Question();
        $question105->setText("Proclaiming the truth of God in an inspiring and enthusiastic manner is something that I have often experiencea.");
        $question105->setCategory("pro");
        $em->persist($question105);

        $question106 = new Question();
        $question106->setText("I've experienced bringing Biblical messages that seem to cut to the heart.");
        $question106->setCategory("pro");
        $em->persist($question106);

        $question107 = new Question();
        $question107->setText("I do not need to be in the public eye to be fulfilled.");
        $question107->setCategory("ser");
        $em->persist($question107);

        $question108 = new Question();
        $question108->setText("I enjoy creative projects and working with my hands.");
        $question108->setCategory("ser");
        $em->persist($question108);

        $question109 = new Question();
        $question109->setText("I would enjoy taking shut-ins out for a drive or assisting them in other practical ways.");
        $question109->setCategory("sho");
        $em->persist($question109);

        $question110 = new Question();
        $question110->setText("I've experienced working joyfully with or helping those people who are ignored by the majority around them.");
        $question110->setCategory("sho");
        $em->persist($question110);

        $question111 = new Question();
        $question111->setText("I find joy in harmonizing and arranging Biblical teaching.");
        $question111->setCategory("tea");
        $em->persist($question111);

        $question112 = new Question();
        $question112->setText("I prefer hearing someone exposit or teach Scriptures more than hearing personal testimonies.");
        $question112->setCategory("tea");
        $em->persist($question112);

        $question113 = new Question();
        $question113->setText("I have spoken in tongues.");
        $question113->setCategory("ton");
        $em->persist($question113);

        $question114 = new Question();
        $question114->setText("When I speak in tongues, I believe it is edifying to the Lord's body through interpretation.");
        $question114->setCategory("ton");
        $em->persist($question114);

        $question115 = new Question();
        $question115->setText("I can intuitively arrive at solutions to complicated problems.");
        $question115->setCategory("wis");
        $em->persist($question115);

        $question116 = new Question();
        $question116->setText("I have felt an unusual presence of God and personal confidence when important decisions needed to be made.");
        $question116->setCategory("wis");
        $em->persist($question116);

        $question117 = new Question();
        $question117->setText("I have been empowered by the Spirit to expel demons in the name of Jesus.");
        $question117->setCategory("mir");
        $em->persist($question117);

        $question118 = new Question();
        $question118->setText("I have seen God intervene and do the impossible through my life.");
        $question118->setCategory("mir");
        $em->persist($question118);

        $question119 = new Question();
        $question119->setText("I am very protective of people under my care.");
        $question119->setCategory("she");
        $em->persist($question119);

        $question120 = new Question();
        $question120->setText("I perceive myself as a shepherd and a teacher of either a small group or a larger group.");
        $question120->setCategory("she");
        $em->persist($question120);

        $question121 = new Question();
        $question121->setText("I enjoy showing others how the Bible speaks to their current situation.");
        $question121->setCategory("pro");
        $em->persist($question121);

        $question122 = new Question();
        $question122->setText("I like to tell others about God's judgment for wrongdoing and of His gracious promises to those who turn to Him.");
        $question122->setCategory("pro");
        $em->persist($question122);

        $question123 = new Question();
        $question123->setText("I like to meet needs immediately.");
        $question123->setCategory("ser");
        $em->persist($question123);

        $question124 = new Question();
        $question124->setText("I am already helping people while others are still talking about it.");
        $question124->setCategory("ser");
        $em->persist($question124);

        $question125 = new Question();
        $question125->setText("I like helping other people and honestly don't expect anything to be done for me in return.");
        $question125->setCategory("sho");
        $em->persist($question125);

        $question126 = new Question();
        $question126->setText("I enjoy rendering physical aid to those who have gotten themselves into trouble.");
        $question126->setCategory("sho");
        $em->persist($question126);

        $question127 = new Question();
        $question127->setText("I like to deduce Biblical principles from my study and then share them with others.");
        $question127->setCategory("tea");
        $em->persist($question127);

        $question128 = new Question();
        $question128->setText("Being able to help other people learn Biblical facts or details which aid in building their lives, satisfies me.");
        $question128->setCategory("tea");
        $em->persist($question128);

        $question129 = new Question();
        $question129->setText("I have complete control of my gift of tongues.");
        $question129->setCategory("ton");
        $em->persist($question129);

        $question130 = new Question();
        $question130->setText("I desire to use my ability to speak an unknown language for evangelism as a sign to unbelievers.");
        $question130->setCategory("ton");
        $em->persist($question130);

        $question131 = new Question();
        $question131->setText("I have seen decisions or suggestions I have made prove to work out well.");
        $question131->setCategory("wis");
        $em->persist($question131);

        $question132 = new Question();
        $question132->setText("I enjoy problem solving, using insights that God gives me from the Bible.");
        $question132->setCategory("wis");
        $em->persist($question132);

        $question133 = new Question();
        $question133->setText("Other people have often perceived God working impossible things through my life.");
        $question133->setCategory("mir");
        $em->persist($question133);

        $question134 = new Question();
        $question134->setText("In the name of the Lord, I have been used to miraculously change circumstances so that God would be glorified.");
        $question134->setCategory("mir");
        $em->persist($question134);

        $question135 = new Question();
        $question135->setText("I enjoy teaching and guiding a group of Christians.");
        $question135->setCategory("she");
        $em->persist($question135);

        $question136 = new Question();
        $question136->setText("I feel that I am responsible to help protect weak Christians from influences that would undermine their faith.");
        $question136->setCategory("she");
        $em->persist($question136);

        $question137 = new Question();
        $question137->setText("I find it easy to apply Biblical promises to human situations.");
        $question137->setCategory("pro");
        $em->persist($question137);

        $question138 = new Question();
        $question138->setText("I feel constrained to speak the truth even at the risk of confronting those in places of authority or those who I would be naturally intimidated by.");
        $question138->setCategory("pro");
        $em->persist($question138);

        $question139 = new Question();
        $question139->setText("I've experienced helping in small ways that often times seem to be behind the scene sort of things.");
        $question139->setCategory("ser");
        $em->persist($question139);

        $question140 = new Question();
        $question140->setText("I've experienced being happy when others get credit for what I do.");
        $question140->setCategory("ser");
        $em->persist($question140);

        $question141 = new Question();
        $question141->setText("I can sense when other people are hurting inside.");
        $question141->setCategory("sho");
        $em->persist($question141);

        $question142 = new Question();
        $question142->setText("I have felt so compassionate for others that I have failed to confront them with the truth when they need it.");
        $question142->setCategory("sho");
        $em->persist($question142);

        $question143 = new Question();
        $question143->setText("I've experienced making difficult Biblical truths understandable to others.");
        $question143->setCategory("tea");
        $em->persist($question143);

        $question144 = new Question();
        $question144->setText("1'm constantly analyzing for better ways to say things.");
        $question144->setCategory("tea");
        $em->persist($question144);

        $question145 = new Question();
        $question145->setText("I desire to use the gift of tongues in an orderly fashion and under the direction of our spiritually mature church leadership.");
        $question145->setCategory("ton");
        $em->persist($question145);

        $question146 = new Question();
        $question146->setText("I have the supernatural ability under the leading of the Holy Spirit to speak in a language I have not learned.");
        $question146->setCategory("ton");
        $em->persist($question146);

        $question147 = new Question();
        $question147->setText("I seem to be able to effectively counsel those people who are \"against a wall\", perplexed, or confused, guilty or addicted.");
        $question147->setCategory("wis");
        $em->persist($question147);

        $question148 = new Question();
        $question148->setText("I have experienced success in helping people choose from various options which often seem very difficult to them but clear to me.");
        $question148->setCategory("wis");
        $em->persist($question148);

        $question149 = new Question();
        $question149->setText("I have sensed a real assurance from God that He will do something through me that would normally be impossible.");
        $question149->setCategory("mir");
        $em->persist($question149);

        $question150 = new Question();
        $question150->setText("God has inspired my prayers so that impossible things have been accomplished.");
        $question150->setCategory("mir");
        $em->persist($question150);

        $question151 = new Question();
        $question151->setText("I am interested in the details of the lives of others so that I can help them grow as Christ's disciples.");
        $question151->setCategory("she");
        $em->persist($question151);

        $question152 = new Question();
        $question152->setText("I've been able to bring back into the fold those individuals who have wandered away.");
        $question152->setCategory("she");
        $em->persist($question152);

        $question153 = new Question();
        $question153->setText("I can accurately spot sin when other people can't.");
        $question153->setCategory("pro");
        $em->persist($question153);

        $question154 = new Question();
        $question154->setText("I've communicated to others timely and urgent messages which I felt came directly from God.");
        $question154->setCategory("pro");
        $em->persist($question154);

        $question155 = new Question();
        $question155->setText("I have enjoyed doing routine tasks that led to more effective ministry by others.");
        $question155->setCategory("ser");
        $em->persist($question155);

        $question156 = new Question();
        $question156->setText("I have a strong desire to meet the practical needs of others.");
        $question156->setCategory("ser");
        $em->persist($question156);

        $question157 = new Question();
        $question157->setText("I can cheerfully spend time with those who need someone to listen to them.");
        $question157->setCategory("sho");
        $em->persist($question157);

        $question158 = new Question();
        $question158->setText("My heart goes out to the poor, the aged, the ill, the underprivileged.");
        $question158->setCategory("sho");
        $em->persist($question158);

        $question159 = new Question();
        $question159->setText("I tend to be more material/content oriented than people or task oriented.");
        $question159->setCategory("tea");
        $em->persist($question159);

        $question160 = new Question();
        $question160->setText("The use of a verse out of context upsets me.");
        $question160->setCategory("tea");
        $em->persist($question160);

        $question161 = new Question();
        $question161->setText("Praying in tongues has been meaningful to me in my personal prayer life.");
        $question161->setCategory("ton");
        $em->persist($question161);

        $question162 = new Question();
        $question162->setText("I never speak in tongues publicly unless I am strongly impressed to do so.");
        $question162->setCategory("ton");
        $em->persist($question162);

        $question163 = new Question();
        $question163->setText("I have a capacity to answer special questions that a non-Christian may have with a very positive impact.");
        $question163->setCategory("wis");
        $em->persist($question163);

        $question164 = new Question();
        $question164->setText("I can see the several sides of an issue and sense which way God is leading.");
        $question164->setCategory("wis");
        $em->persist($question164);

        $question165 = new Question();
        $question165->setText("I believe that God can miraculously alter circumstances if we pray.");
        $question165->setCategory("mir");
        $em->persist($question165);

        $question166 = new Question();
        $question166->setText("The Holy Spirit works to change situations when I pray.");
        $question166->setCategory("mir");
        $em->persist($question166);

        $question167 = new Question();
        $question167->setText("I've a great desire to give direction to those under my care and to look after their spiritual welfare with them.");
        $question167->setCategory("she");
        $em->persist($question167);

        $question168 = new Question();
        $question168->setText("My life revolves around people -one person after another -I love people.");
        $question168->setCategory("she");
        $em->persist($question168);

        $question169 = new Question();
        $question169->setText("I have given messages of warning, judgment or direction from the Lord either privately or publicly.");
        $question169->setCategory("pro");
        $em->persist($question169);

        $question170 = new Question();
        $question170->setText("When I speak my desire is that God would convict men and women's hearts that they might see Jesus.");
        $question170->setCategory("pro");
        $em->persist($question170);

        $question171 = new Question();
        $question171->setText("My ministry consists of watching for unmet needs and then quietly meeting those needs.");
        $question171->setCategory("ser");
        $em->persist($question171);

        $question172 = new Question();
        $question172->setText("I like to have a good leader that I can support in practical and meaningful ways.");
        $question172->setCategory("ser");
        $em->persist($question172);

        $question173 = new Question();
        $question173->setText("I am an emotional person -I cry easily.");
        $question173->setCategory("sho");
        $em->persist($question173);

        $question174 = new Question();
        $question174->setText("I find it easy to express myself on a one-to-one basis and I am outgoing in a soft-spoken way.");
        $question174->setCategory("sho");
        $em->persist($question174);

        $question175 = new Question();
        $question175->setText("I devote time to learning new Biblical truths to communicate to others.");
        $question175->setCategory("tea");
        $em->persist($question175);

        $question176 = new Question();
        $question176->setText("I would rather research and read than meet with people.");
        $question176->setCategory("tea");
        $em->persist($question176);

        $question177 = new Question();
        $question177->setText("I feel I lack the words to praise God as I wish I could.");
        $question177->setCategory("ton");
        $em->persist($question177);

        $question178 = new Question();
        $question178->setText("When I first prayed in tongues, no one pressured me to do so.");
        $question178->setCategory("ton");
        $em->persist($question178);

        $question179 = new Question();
        $question179->setText("Others tell me that I show maturity in offering advise about spiritual matters.");
        $question179->setCategory("wis");
        $em->persist($question179);

        $question180 = new Question();
        $question180->setText("God has given me a wisdom far beyond my natural abilities.");
        $question180->setCategory("wis");
        $em->persist($question180);

        // Send everything to the database!
        $em->flush();

        return new Response('Created the questions!');
    }
}