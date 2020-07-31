using System;
using Microsoft.Azure.WebJobs;
using Microsoft.Azure.WebJobs.Host;
using Microsoft.Extensions.Logging;
using SolaceSystems.Solclient.Messaging;
using System.Threading;
using System.Text;

namespace SB2SolaceCSharp
{
    public static class Function1
    {
        private static SolacePublisher solaceConnection = new SolacePublisher(
            Environment.GetEnvironmentVariable("solace-host"),
            Environment.GetEnvironmentVariable("solace-username"),
            Environment.GetEnvironmentVariable("solace-password"),
            Environment.GetEnvironmentVariable("solace-vpnname"),
            Environment.GetEnvironmentVariable("solace-topic"));

        [FunctionName("Function1")]
        public static void Run([ServiceBusTrigger("azure2solacecsharp", Connection = "SBConnection")]string myQueueItem, ILogger log)
        {
            log.LogInformation($">>>>>>>>>>>>>>>>>>>>>>>C# ServiceBus queue trigger function processed message: {myQueueItem}");
            solaceConnection.sendMessage2Solace(myQueueItem);
        }
    }
}
