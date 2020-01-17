package com.interview.Bot;
import java.io.IOException;
import java.util.concurrent.atomic.AtomicLong;

import org.springframework.http.HttpHeaders;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.ModelAndView;

import com.interview.Bot.Subjective.SubmitSubjective;

@RestController
public class BotController {
	
/*	@GetMapping("/subjective")
	public int subjective(@RequestParam(value = "name", defaultValue = "World") String answer, int question_id, int userId) {
		int score = 0 ;
		System.out.println("test >> ");
		return score;
	}
	*/
	@RequestMapping(value = "/subjective", method = RequestMethod.POST)
	public String subjective(@RequestBody String dataString,String questionId,String email) throws IOException, InterruptedException {
		int score = 0 ;
		SubmitSubjective.submitSubStr(dataString, questionId,email);
		return "data_String";
	}
/*
	@RequestMapping(value = "/quiz", method = RequestMethod.POST)
	public ModelAndView quiz(@ModelAttribute String email,String exp) {
		System.out.println(">>");
	    ModelAndView modelAndView = new ModelAndView();
	    modelAndView.setViewName("quiz.html");
		return modelAndView;
	}*/
	
	@RequestMapping(value= "/quiz" ,method = RequestMethod.POST)
	public String quiz(@RequestBody String email,String exp) {
		System.out.println("email " +email);
	    ModelAndView modelAndView = new ModelAndView();
	    modelAndView.setViewName("/");    
	    return email;

	}
	
	@RequestMapping(value= "/quizSubmit" ,method = RequestMethod.POST)
	public String submitScore(@RequestBody String score, String email) {
		System.out.println(">> " +email);
		System.out.println(">> " +score);
	    return "success";

	}
	
	@RequestMapping("/")
	public ModelAndView index () {
	    ModelAndView modelAndView = new ModelAndView();
	    modelAndView.setViewName("home.html");
	    return modelAndView;
	}
	/*@GetMapping("/quizAns")
	public int subjective(@RequestParam(value = "name", defaultValue = "World") String answer, int id) {
		int score = 0 ;
		return score;
	}*/
	

}
