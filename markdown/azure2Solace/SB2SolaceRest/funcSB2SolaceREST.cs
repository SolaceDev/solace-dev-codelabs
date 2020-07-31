using System;
using System.Net.Http;
using System.Reflection;
using System.Text;
using Microsoft.AspNetCore.Http;
using Microsoft.Azure.WebJobs;
using Microsoft.Azure.WebJobs.Host;
using Microsoft.Extensions.Logging;

namespace SB2SolaceRest
{
    public static class funcSB2SolaceREST
    {
        private static readonly HttpClient _Client = new HttpClient();
        private static string solaceRESTUrl = null;
        private static Boolean init = initializeHttpClient();

        [FunctionName("funcSB2SolaceREST")]
        public static async void Run([ServiceBusTrigger("azure2solacerest", Connection = "SBConnection")] string myQueueItem, ILogger log)
        {
            log.LogInformation($"C# ServiceBus queue trigger function processed message: {myQueueItem}");
            if (initializeHttpClient())
            {
                HttpRequestMessage httpRequestMessage = new HttpRequestMessage
                {
                    Method = HttpMethod.Post,
                    RequestUri = new Uri(solaceRESTUrl)
                };
                HttpContent httpContent = new StringContent(myQueueItem, Encoding.UTF8, "application/text");
                httpRequestMessage.Content = httpContent;
                var response = await _Client.SendAsync(httpRequestMessage);
                string responseString = await response.Content.ReadAsStringAsync();
                log.LogInformation($"Response from Solace :{responseString}, Response Code :{response.StatusCode}");
            }
            else
            {
                log.LogInformation("Unable to initialize HTTP Client");
                throw new Exception("Unable to initialize HTTP Client");
            }
        }

        public static bool initializeHttpClient()
        {
            if (!init)
            {
                string username = Environment.GetEnvironmentVariable("solace-username");
                string password = Environment.GetEnvironmentVariable("solace-password");
                string auth = "Basic " + Convert.ToBase64String(Encoding.UTF8.GetBytes($"{username}:{password}"));
                _Client.DefaultRequestHeaders.Add("Authorization", auth);
                string port = null;
                string protocol = "http";
                if (Boolean.Parse(Environment.GetEnvironmentVariable("solace-tls")))
                {
                    port = Environment.GetEnvironmentVariable("solace-tls-port");
                    protocol = "https";
                    //TODO: If 2 -way TLS, we may need to add Cert related stuff
                }
                else
                    port = Environment.GetEnvironmentVariable("solace-plain-text-port");
                solaceRESTUrl = protocol + "://" + Environment.GetEnvironmentVariable("solace-host") + ":" + port +
                                "/" + Environment.GetEnvironmentVariable("solace-topic");
                init = true;
            }
            return init;
        }
    }

}

