using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net.Http;
using System.Net;

namespace Microsoft.Samples.Kinect.BodyBasics
{
    public class MyHttpClient
    {
        static String baseUrl = "http://127.0.0.1/";

        static String volume = "volume/";
        static String start = "start/";
        static String beat = "beat/";
        static String play = "play";
        static String pause = "pause/";

        public static void startTone(String id)
        {
            String url = baseUrl + start + id;

            using (var client = new WebClient())
            {
                var responseString = client.DownloadString(url);
            }
        }

        public static void playTone(String id)
        {
            String url = baseUrl + play + id;

            using (var client = new WebClient())
            {
                var responseString = client.DownloadString(url);
            }
        }

        public static void pauseTone(String id)
        {
            String url = baseUrl + pause + id;

            using (var client = new WebClient())
            {
                var responseString = client.DownloadString(url);
            }
        }

        public static async void changeVolume(String value , String id)
        {
            String url = baseUrl + volume + id;
            using (var client = new HttpClient())
            {
                var values = new List<KeyValuePair<string, string>>();
                values.Add(new KeyValuePair<string, string>("value", value));

                var content = new FormUrlEncodedContent(values);
                var response = await client.PostAsync(url, content);
                var responseString = await response.Content.ReadAsStringAsync();
            }
        }

        public static async void changeBeat(String value, String id)
        {
            String url = baseUrl + beat + id;
            using (var client = new HttpClient())
            {
                var values = new List<KeyValuePair<string, string>>();
                values.Add(new KeyValuePair<string, string>("value", value));

                var content = new FormUrlEncodedContent(values);
                var response = await client.PostAsync(url, content);
                var responseString = await response.Content.ReadAsStringAsync();
            }
        }

    }
}
