
import java.io.*;
import java.util.*;

// import javax.activation.*;
// import javax.mail.*;
// import javax.mail.internet.*;
public class Send_Email {
	static final String username = "pckkkh";
	static final String email = username + "@yahoo.com";
	static final String password = "Kellen2000";

	static Scanner scan;

	public static void main(String[] args) {
		File file = new File("input.txt");
		// GUI popup = new GUI();

		StringBuilder output = new StringBuilder();

		try {
			scan = new Scanner(file);
		} catch (Exception e) {
			// popup.updateText("File not found: input.txt");
			return;
		}

		String all = "";
		while (scan.hasNext()) {
			all += scan.nextLine() + "\n";
		}

		// Properties props = new Properties();
		// props.setProperty("mail.transport.protocol", "smtp");
		// props.setProperty("mail.host", "smtp.live.com");
		// props.put("mail.smtp.starttls.enable", "true");
		// props.put("mail.smtp.auth", "true");

		// props.put("mail.smtp.starttls.enable", "true");
		// props.put("mail.smtp.host", "smtp.mail.yahoo.com");
		// props.put("mail.smtp.auth", "true");
		// props.put("mail.debug", "false");
		// props.put("mail.smtp.port", "587");
		// props.put("mail.smtp.user", email);
		// props.put("mail.smtp.password", password);

		// Session session = Session.getInstance(props,
		// new javax.mail.Authenticator() {
		// protected PasswordAuthentication getPasswordAuthentication() {
		// return new PasswordAuthentication(email, password);
		// }
		// });

		String[] persons = all.split(";");

		// popup.updateText("Created Connection.\nSending " + persons.length + "
		// emails");
		output.append("Results | Sending " + persons.length + " email(s)\n\n");

		int index = 1;
		for (String person : persons) {
			System.out.println("Person: " + person);
			String[] parts = person.split("/");
			String name = parts[0];
			String mail = parts[1];
			String subject = parts[2];
			String text = parts[3]; // <img src="image.jpg"/>
			int attachmentIndex = 4;

			output.append(index).append(". ").append(name).append(": ");

			try {

				// Message message = new MimeMessage(session);
				// message.setFrom(new InternetAddress(email));
				// message.setRecipients(Message.RecipientType.TO,
				// InternetAddress.parse(mail));
				// message.setSubject(subject);
				// message.setText(text);

				if (parts.length > attachmentIndex) {
					// Multipart multipart = new MimeMultipart("related");

					for (int i = attachmentIndex; i < parts.length; i++) {
						parts[i] = parts[i].replaceAll("\n", "");
						String id = "image" + i;

						// MimeBodyPart messageBodyPart = new MimeBodyPart();
						String htmlText = i == attachmentIndex ? "<p>" + text + "</p>"
								: "" + "<img src=\"cid:" + id + "\">";
						// messageBodyPart.setContent(htmlText, "text/html");
						// multipart.addBodyPart(messageBodyPart);

						// messageBodyPart = new MimeBodyPart();
						// DataSource fds = new FileDataSource(System.getProperty("user.dir") + "/" +
						// parts[i]);
						// messageBodyPart.setDataHandler(new DataHandler(fds));
						// messageBodyPart.setHeader("Content-ID","<image>");
						// messageBodyPart.setFileName(parts[i]);
						// multipart.addBodyPart(messageBodyPart);
						// popup.updateText("Attached: image" + i);

					}
					// message.setContent(multipart);
				}
				// popup.updateText("Sending");
				// Transport.send(message);

				// popup.updateText(index + ". Sent the email: " + subject + " to: " + mail);

				// popup.updateText(index + ". Sent the email: " + subject + " to: " + mail);
				output.append(index + ". Success");

			} catch (Exception e) {
				// popup.updateText(index + ". Cannot send the email: " + subject + " to " +
				// mail);
				e.printStackTrace();
				output.append(index + ". Fail. Email not sent!");
			}
			index++;
		}

		// popup.updateText("All Done!");
		output.append("\nDone: Sending " + persons.length + " emails\n\n\n\nInput:\n").append(all);
		scan.close();

		// if(file.delete())
		// {
		// popup.updateText("File deleted successfully");
		// }
		// else
		// {
		// popup.updateText("Failed to delete the file");
		// }

		File resultsFile = new File("results.txt");
		resultsFile.delete();

		try {
			PrintWriter writer = new PrintWriter(new File("results.txt"));
			writer.println(output);
			writer.close();
		} catch (FileNotFoundException e) {
			// popup.updateText("Cannot write results to text");
			e.printStackTrace();
		}
	}

}
