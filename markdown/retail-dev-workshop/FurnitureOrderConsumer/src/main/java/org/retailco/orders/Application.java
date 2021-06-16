
package org.retailco.orders;


import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

import java.util.function.Consumer;


@SpringBootApplication
public class Application {

	private static final Logger logger = LoggerFactory.getLogger(Application.class);

	public static void main(String[] args) {
		SpringApplication.run(Application.class);
	}

	@Bean
	public Consumer<OrderValidated> retailcoOrderUpdateValidatedV1B2CFurnitureConsumer() {
    return furnitureOrderValidated -> {
      logger.info("Received Furniture Order Validated Event: " + furnitureOrderValidated.toString());
    };
	}

  

}
