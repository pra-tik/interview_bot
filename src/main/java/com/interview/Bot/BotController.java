package com.interview.Bot;
import java.util.concurrent.atomic.AtomicLong;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.ModelAndView;

import com.interview.Bot.Subjective.SubmitSubjective;

@Controller
public class BotController {
	
/*	@GetMapping("/subjective")
	public int subjective(@RequestParam(value = "name", defaultValue = "World") String answer, int question_id, int userId) {
		int score = 0 ;
		System.out.println("test >> ");
		return score;
	}
	*/
	@RequestMapping(value = "/subjective", method = RequestMethod.POST)
	public String subjective(@RequestBody String dataString,String questionId) {
		int score = 0 ;
		SubmitSubjective.submitSubStr(dataString, questionId);
		return "data_String";
	}

	@RequestMapping(value = "/quiz", method = RequestMethod.POST)
	public ModelAndView quiz(@RequestBody String email,String exp) {
	    ModelAndView modelAndView = new ModelAndView();
	    modelAndView.setViewName("quiz.html");
		return modelAndView;
	}
	@RequestMapping("/")
	public ModelAndView index () {
	    ModelAndView modelAndView = new ModelAndView();
	    modelAndView.setViewName("index.html");
	    return modelAndView;
	}
	/*@GetMapping("/quizAns")
	public int subjective(@RequestParam(value = "name", defaultValue = "World") String answer, int id) {
		int score = 0 ;
		return score;
	}*/
	

}
