using System;
using SolaceSystems.Solclient.Messaging;
using System.Threading;
using System.Text;

namespace SB2SolaceCSharp
{
    public class SolacePublisher
    {
        private IContext context = null;
        private ISession session = null;

        private string sUserName = "default";
        private string sPassword = "default";
        private string sVPNName = "default";
        private string sHost = "default";
        private string sTopic = "default";

        //public Object lockThis = new Object();


        public SolacePublisher(string Host, string UserName, string Password, string VPNName, string Topic)
        {
            this.sHost = Host;
            this.sUserName = UserName;
            this.sPassword = Password;
            this.sVPNName = VPNName;
            this.sTopic = Topic;
            connect2Solace();
        }

        ~SolacePublisher()
        {
            Console.WriteLine("In destructor - Will try to dispose session and context");
            if (session != null)
            {
                session.Disconnect();
                session.Dispose();
                session = null;
                Console.WriteLine("In destructor - disposed session");
            }
            if (context != null)
            {
                context.Dispose();
                context = null;
                Console.WriteLine("In destructor - disposed context");
            }

        }

        public void sendMessage2Solace(String msg)
        {
            IMessage message = ContextFactory.Instance.CreateMessage();
            message.Destination = ContextFactory.Instance.CreateTopic(sTopic);
            message.DeliveryMode = MessageDeliveryMode.Direct;
            message.BinaryAttachment = Encoding.ASCII.GetBytes(msg);

            Console.WriteLine("About to send message '{0}' to topic '{1}'", msg, sTopic);
            session.Send(message);
            message.Dispose();
            Console.WriteLine("Message sent. Exiting.");

        }

        public void connect2Solace()
        {
            Console.WriteLine("In connect2Solace");
            ContextFactoryProperties cfp = new ContextFactoryProperties();

            // Set log level.
            cfp.SolClientLogLevel = SolLogLevel.Warning;
            // Log errors to console.
            cfp.LogToConsoleError();
            // Must init the API before using any of its artifacts.
            ContextFactory.Instance.Init(cfp);
            ContextProperties contextProps = new ContextProperties();
            SessionProperties sessionProps = new SessionProperties();

            /******** Delete This ***********/
            sHost = "54.219.47.90";
            sUserName = "default";
            sPassword = "default";
            sVPNName = "default";
            /********************************/
            sessionProps.Host = sHost;
            sessionProps.UserName = sUserName;
            sessionProps.Password = sPassword;
            sessionProps.SSLValidateCertificate = false;
            sessionProps.VPNName = sVPNName;

            //Connection retry logic
            sessionProps.ConnectRetries = 3; //-1 means try to connect forever.
            sessionProps.ConnectTimeoutInMsecs = 5000; //10 seconds
            sessionProps.ReconnectRetries = 3; //-1 means try to reconnect forever.
            sessionProps.ReconnectRetriesWaitInMsecs = 5000; //wait for 5 seconds before retry

            // Compression is set as a number from 0-9, where 0 means "disable
            // compression", and 9 means max compression. The default is no
            // compression.
            // Selecting a non-zero compression level auto-selects the
            // compressed SMF port on the appliance, as long as no SMF port is
            // explicitly specified.
            //sessionProps.CompressionLevel = 9;

            #region Create the Context

            context = ContextFactory.Instance.CreateContext(contextProps, null);

            #endregion

            #region Create and connect the Session
            session = context.CreateSession(sessionProps, null, null);
            session.Connect();
            #endregion
        }
    }
}
