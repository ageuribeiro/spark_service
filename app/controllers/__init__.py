from flask import Flask, Blueprint

def register_controllers(app):
    from .person_controller import person_bp
    from .academy_controller import academy_bp
    from .log_controller import log_bp
    from .access_log_controller import access_log_bp
    from .exercise_controller import exercise_bp
    from .financial_controller import financial_bp
    from .membership_controller import membership_bp
    from .training_exercise_controller import training_exercise_bp
    from .training_plan_controller import training_plan_bp
    from .user_controller import user_bp
    # Importar todos os blueprints dos controllers


    app.register_blueprint(person_bp, url_prefix='/persons')
    app.register_blueprint(academy_bp, url_prefix='/academies')
    app.register_blueprint(log_bp, url_prefix='/logs')
    app.register_blueprint(access_log_bp, url_prefix='/access_log')
    app.register_blueprint(exercise_bp, url_prefix='/exercise')
    app.register_blueprint(financial_bp, url_prefix='/financial')
    app.register_blueprint(membership_bp, url_prefix='/membership')
    app.register_blueprint(training_exercise_bp, url_prefix='/training_exercise')
    app.register_blueprint(training_plan_bp, url_prefix='/training_plan')
    app.register_blueprint(user_bp, url_prefix='/user_bp')

    # Registrar todos os blueprints