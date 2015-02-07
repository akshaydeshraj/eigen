using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net.Http;
using System.Net;
using System.IO;
using System.Collections.Specialized;

namespace Microsoft.Samples.Kinect.BodyBasics
{
    public class EigenRequest
    {
        static String baseUrl = "http://localhost";

        static String volume = "/volume";
        static String start = "/start";
        static String beat = "/beat";
        static String play = "/play";
        static String pause = "/pause";

        public static void get(String url)
        {
            // Get request function

            HttpWebRequest request = (HttpWebRequest)WebRequest.Create(url);
            HttpWebResponse response = (HttpWebResponse)request.GetResponse();
            Stream stream = response.GetResponseStream();
            StreamReader reader = new StreamReader(stream);
            string data = reader.ReadToEnd();

            reader.Close();
            stream.Close();

        }

        public static void post(String url, String value)
        {
            // Post request function

            using(WebClient client = new WebClient()){
            byte[] response = client.UploadValues(url, new NameValueCollection()
                {
                    { "value", value }
                });
            }
        }

        // Callable functions

        public static void startLoop(String id)
        {
            // Start looping music of given id

            String uri = baseUrl + start + "/" + id;
            get(uri);
        }

        public static void pauseMusic(String id)
        {
            // Pause music of given id

            String uri = baseUrl + pause + "/" + id;
        }

        public static void playMusic(String id)
        {
            // Play music of given id

            String uri = baseUrl + play + "/" + id;
        }

        public static void changeVolume(String id, String value)
        {
            // Change volume

            String uri = baseUrl + volume + "/" + id;
            post(uri, value);
        }

        public static void changeBPM(String id, String value)
        {
            // Change tempo (BPM)

            String uri = baseUrl + beat + "/" + id;
            post(uri, value);
        }

    }
}
