from colors.colors import Color
from presentation.gui import GUI
from presentation.console import Console
from presentation.settings import Settings, SettingsManager
from services.client_services import ClientService
from services.movie_services import MovieService
from services.rental_service import RentalService
from validation.client_validator import ClientValidator
from validation.movie_validator import MovieValidator
from validation.rental_validator import RentalValidator

if __name__ == "__main__":
    try:
        movie_validator = MovieValidator()
        client_validator = ClientValidator()
        rental_validator = RentalValidator()

        settings = Settings()
        settings.load_data()
        options = settings.get_options()
        ui_option, movie_repository, client_repository, rental_repository = SettingsManager().configure_options(options)

        movie_service = MovieService(movie_validator, movie_repository)
        client_service = ClientService(client_validator, client_repository)
        rental_service = RentalService(rental_validator, rental_repository, movie_repository, client_repository)

        SettingsManager().configure_populate(options, movie_service, client_service)

        if ui_option == 1:
            console = Console(movie_service, client_service, rental_service)
            console.run()
        elif ui_option == 2:
            gui = GUI(movie_service, client_service, rental_service)
            gui.run()
    except Exception as exception:
        print(Color.FAIL + 'Unexpected exception occurred:\n' + str(exception) + Color.ENDC)
