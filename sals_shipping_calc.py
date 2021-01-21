
def ground_shipping_cost(weight):

  if weight <= 2:
    price_per_pound = 1.50
  elif weight <=6:
    price_per_pound = 3.00
  elif weight <=10:
    price_per_pound = 4.00
  else:
    price_per_pound = 4.75
    
  return 20.0 + (weight * price_per_pound) 
  


premium_ground_shipping = 125.0

def drone_shipping_cost(weight):

  if weight <= 2:
    price_per_pound = 4.50
  elif weight <=6:
    price_per_pound = 9.00
  elif weight <=10:
    price_per_pound = 12.00
  else:
    price_per_pound = 14.25
    
  return (weight * price_per_pound) 



def print_cheapest_method(weight):

    ground = ground_shipping_cost(weight)
    premium = premium_ground_shipping
    drone = drone_shipping_cost(weight)

    if ground < premium and ground < drone:
        method = "standard ground"
        cost = ground
    elif premium < ground and premium < drone:
      method = "premium"
      cost = premium
    else:
        method = "drone" 
        cost = drone

    print(
        "The cheapest option available is $%.2f with %s shipping."
    % (cost, method)
    )

print_cheapest_method(15)




