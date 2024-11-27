def register_controllers(app):
    from .person_controller import person_bp
    from .academy_controller import academy_bp
    from .log_controller import log_bp
    # Importar todos os blueprints dos controllers


    app.register_blueprint(person_bp, url_prefix='/persons')
    app.register_blueprint(academy_bp, url_prefix='/academies')
    app.register_blueprint(log_bp, url_prefix='/logs')
    # Registrar todos os blueprints