package com.interview.Bot.Subjective;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;

public class SubmitSubjective {

	public static void submitSubStr(String answer, String questionId, String email)
			throws IOException, InterruptedException {
		System.out.println("" + "\n QuestionID :  " + questionId + "\n Answer : " + answer);
		String[] answerAry = answer.replace("dataString=", "").split("&");
		System.out.println("ans > "+answer);
		Process proc = Runtime.getRuntime().exec("python3 /home/pcadmin/Desktop/Bot/src/main/resources/static/p/user_score.py " + answerAry[0]);

		BufferedReader stdInput = new BufferedReader(new InputStreamReader(proc.getInputStream()));

		BufferedReader stdError = new BufferedReader(new InputStreamReader(proc.getErrorStream()));

		// Read the output from the command
		System.out.println("Here is the standard output of the command:\n");
		String s = null;
		while ((s = stdInput.readLine()) != null) {
			System.out.println(s);
		}

		// Read any errors from the attempted command
		System.out.println("Here is the standard error of the command (if any):\n");
		while ((s = stdError.readLine()) != null) {
			System.out.println(s);
		}

	}
}
