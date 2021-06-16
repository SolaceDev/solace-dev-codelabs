
package org.retailco.orders;

import com.fasterxml.jackson.annotation.JsonInclude;


@JsonInclude(JsonInclude.Include.NON_NULL)
public class OrderValidated {

	public OrderValidated () {
	}
	public OrderValidated (
		String totalPrice, 
		String channel, 
		String id, 
		String type, 
		String validationStatus, 
		String timestamp) {
		this.totalPrice = totalPrice;
		this.channel = channel;
		this.id = id;
		this.type = type;
		this.validationStatus = validationStatus;
		this.timestamp = timestamp;
	}


	private String totalPrice;
	private String channel;
	private String id;
	private String type;
	private String validationStatus;
	private String timestamp;

	public String getTotalPrice() {
		return totalPrice;
	}

	public OrderValidated setTotalPrice(String totalPrice) {
		this.totalPrice = totalPrice;
		return this;
	}


	public String getChannel() {
		return channel;
	}

	public OrderValidated setChannel(String channel) {
		this.channel = channel;
		return this;
	}


	public String getId() {
		return id;
	}

	public OrderValidated setId(String id) {
		this.id = id;
		return this;
	}


	public String getType() {
		return type;
	}

	public OrderValidated setType(String type) {
		this.type = type;
		return this;
	}


	public String getValidationStatus() {
		return validationStatus;
	}

	public OrderValidated setValidationStatus(String validationStatus) {
		this.validationStatus = validationStatus;
		return this;
	}


	public String getTimestamp() {
		return timestamp;
	}

	public OrderValidated setTimestamp(String timestamp) {
		this.timestamp = timestamp;
		return this;
	}


	public String toString() {
		return "OrderValidated ["
		+ " totalPrice: " + totalPrice
		+ " channel: " + channel
		+ " id: " + id
		+ " type: " + type
		+ " validationStatus: " + validationStatus
		+ " timestamp: " + timestamp
		+ " ]";
	}
}

