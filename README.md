# luigi_expt
experimenting with Luigi workflow

## Test case:
#### Here is a simple scneario to build a conditional workflow using Luigi
##### Tasks at hand
- Clean the car (CleanCar)
- pick items from a bigbox store (PickItem)
- Parallelly, get money transfered to your account (MoneyTransfer)
- Get the Fuel to the car. (GetFuel). The Fuel station may take some time between 10m and 40m.
- If the time taken at the Fuel station is less than 15m (condition)
- If 'condition' is True, go to library and pick the book (PickBook)
- Go to home (GoHome)
