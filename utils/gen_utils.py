"""General utility methods."""
import logging


logger = logging.getLogger(__name__)

class classproperty:
    """Allows function to be accessed as a class level property.

    Example:
    .. code-block::

        class LogisticRegressionBinaryPipeline(PipelineBase):
            component_graph = ['Simple Imputer', 'Logistic Regression Classifier']

            @classproperty
            def summary(cls):
            summary = ""
            for component in cls.component_graph:
                component = handle_component_class(component)
                summary += component.name + " + "
            return summary

        assert LogisticRegressionBinaryPipeline.summary == "Simple Imputer + Logistic Regression Classifier + "
        assert LogisticRegressionBinaryPipeline().summary == "Simple Imputer + Logistic Regression Classifier + "
    """

    def __init__(self, func):
        self.func = func

    def __get__(self, _, klass):
        """Get property value."""
        return self.func(klass)