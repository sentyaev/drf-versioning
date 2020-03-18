class SerializerClassMixin:
    version_map = None

    def _get_serializer_class(self, version):
        return self.version_map[version]

    def get_serializer_class(self):
        if not self.version_map:
            raise Exception(f'Version Map not provided for {self.__class__.__name__}')

        version = self.request.version
        return self._get_serializer_class(version)
